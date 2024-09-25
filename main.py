from pieces import Pawn, Rook, Bishop, Knight, Queen, King
import pygame as pg


class Game:
    def __init__(self):
        """_summary_"""
        self.screen = pg.display.set_mode((600, 600))
        self.clock = pg.time.Clock()
        self.running = True
        self.board_image = pg.image.load("assets/images/board.png")
        self.board_image = pg.transform.scale(self.board_image, (600, 600))
        self.title = pg.display.set_caption("Chess by Marek B")
        self.icon = pg.image.load("assets/images/chess_icon.png")
        self.set_icon = pg.display.set_icon(self.icon)
        self.figures = {}
        self.highlighted_cells = set()

    def add_figure(self, figure_type, x, y, color):
        """_summary_

        Args:
            figure_type (_type_): _description_
            x (_type_): _description_
            y (_type_): _description_
            color (_type_): _description_
        """
        figure_class = globals()[figure_type]
        figure = figure_class(color)
        figure.screen = self.screen
        figure.load_image(f"assets/images/{color}/{figure_type.lower()}.png")

        self.figures[(x, y)] = figure

    def draw_figures(self):
        """_summary_"""
        for position, figure in self.figures.items():
            figure.draw(*position)

    def highlight_cell(self, x, y):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_
        """
        pg.draw.rect(self.screen, "#e16954", (x * 75, y * 75, 75, 75))

    def run(self):
        """_summary_"""
        while self.running:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos[0] // 75, event.pos[1] // 75
                    if event.button == 1:  # Right mouse button
                        self.highlighted_cells.clear()
                    elif event.button == 3:  # Left mouse button
                        self.highlighted_cells.add((x, y))

            self.screen.blit(self.board_image, (0, 0))

            for x, y in self.highlighted_cells:
                self.highlight_cell(x, y)

            self.draw_figures()

            pg.display.flip()
            pg.display.update()

        pg.quit()


if __name__ == "__main__":
    game = Game()

    figures = {
        "Rook": [0, 7],
        "Knight": [1, 6],
        "Bishop": [2, 5],
        "Queen": [3],
        "King": [4],
    }

    # Add rooks, knights, bishops, queens, kings

    for figure_type, positions in figures.items():
        for pos in positions:
            game.add_figure(figure_type, pos, 7, "white")
            game.add_figure(figure_type, pos, 0, "black")

    # Add pawns

    for x_cell in range(8):
        game.add_figure("Pawn", x_cell, 6, "white")
        game.add_figure("Pawn", x_cell, 1, "black")

    game.run()
