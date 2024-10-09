from pieces import Pawn, Rook, Bishop, Knight, Queen, King
import pygame as pg

class PieceManager:
    def __init__(self, screen):
        self.figures = {}
        self.selected_piece = None
        self.dot_image = pg.image.load("assets/images/dot.png")
        self.dot_image = pg.transform.scale(self.dot_image, (75, 75))
        self.highlighted_cells = set()
        self.selected_cells = set()
        self.screen = screen

    def add_figure(self, figure_type, x, y, color):
        figure_class = globals()[figure_type]
        figure = figure_class(color)
        figure.screen = self.screen
        figure.load_image(f"assets/images/{color}/{figure_type.lower()}.png")
        figure.position = (x, y)
        self.figures[(x, y)] = {"piece": figure, "position": (x, y)}

    def draw_figures(self):
        for position, figure_data in self.figures.items():
            figure = figure_data["piece"]
            figure.draw(*position)

    def highlight_pawn_moves(self, x, y, color):
        direction = -1 if color == "white" else 1

        # Move one space forward
        if 0 <= y + direction < 8:
            self.highlighted_cells.add((x, y + direction))

        # Move two spaces forward (only on beginning)
        if (
            (color == "white" and y == 1) or (color == "black" and y == 6)
        ) and 0 <= y + 2 * direction < 8:
            self.highlighted_cells.add((x, y + 2 * direction))

    def highlight_rook_moves(self, x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                self.highlighted_cells.add((nx, ny))
                nx += dx
                ny += dy

    def highlight_bishop_moves(self, x, y):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                self.highlighted_cells.add((nx, ny))
                nx += dx
                ny += dy

    def highlight_knight_moves(self, x, y):
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                self.highlighted_cells.add((nx, ny))

    def highlight_queen_moves(self, x, y):
        self.highlight_rook_moves(x, y)
        self.highlight_bishop_moves(x, y)

    def highlight_king_moves(self, x, y):
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                self.highlighted_cells.add((nx, ny))

    def highlight_possible_moves(self):
        if self.selected_piece:
            piece_data = self.figures[self.selected_piece]
            x, y = piece_data["position"]
            figure = piece_data["piece"]

            # Show every possible move for each piece
            if isinstance(figure, Pawn):
                self.highlight_pawn_moves(x, y, figure.color)
            elif isinstance(figure, Rook):
                self.highlight_rook_moves(x, y)
            elif isinstance(figure, Bishop):
                self.highlight_bishop_moves(x, y)
            elif isinstance(figure, Knight):
                self.highlight_knight_moves(x, y)
            elif isinstance(figure, Queen):
                self.highlight_queen_moves(x, y)
            elif isinstance(figure, King):
                self.highlight_king_moves(x, y)

    def highlight_cell(self, x, y):
        pg.draw.rect(self.screen, "#e16954", (x * 75, y * 75, 75, 75))

    def draw_dot(self, x, y):
        self.screen.blit(self.dot_image, (x * 75, y * 75))

    def move_piece(self, x, y):
        piece_data = self.figures[self.selected_piece]
        figure = piece_data["piece"]

        # Remove the piece from its current position
        del self.figures[self.selected_piece]

        # Add the piece to its new position
        self.figures[(x, y)] = {"piece": figure, "position": (x, y)}
        figure.position = (x, y)

        self.highlighted_cells.clear()
        self.selected_piece = None

    def handle_click(self, x, y, button):
        if button == 1:  # Left mouse button
            self.selected_cells.clear()  # Clear every selected cell
            
            if (x, y) in self.highlighted_cells:
                self.move_piece(x, y)
            else:
                piece_key = (x, y)
                if piece_key in self.figures:
                    if self.selected_piece == piece_key:
                        # Double click on the same piece to deselect it
                        self.highlighted_cells.clear()
                    else:
                        self.selected_piece = piece_key
                        self.highlight_possible_moves()
                else:
                    self.selected_piece = None
                    self.highlighted_cells.clear()
        elif button == 3:  # Right mouse button
            if (x, y) in self.selected_cells:
                self.selected_cells.remove((x, y))
            else:
                self.selected_cells.add((x, y))


