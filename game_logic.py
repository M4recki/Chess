import pygame as pg
from board import Board
from piece_manager import PieceManager

class GameLogic:
    def __init__(self):
        self.board = Board()
        self.piece_manager = PieceManager(self.board.screen)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.board.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos[0] // 75, event.pos[1] // 75
                self.piece_manager.handle_click(x, y, event.button)
            
    def update_game_state(self):
        pass
    
    def draw_everything(self):
        self.board.screen.blit(self.board.board_image, (0, 0))
        
        # Draw dots for possible moves
        for x, y in self.piece_manager.highlighted_cells:
            self.piece_manager.draw_dot(x, y)
        
        # Draw selected cells with red color
        for x, y in self.piece_manager.selected_cells:
            self.piece_manager.highlight_cell(x, y)
        
        self.piece_manager.draw_figures()

    def run(self):
        while self.board.running:
            self.handle_events()
            self.update_game_state()
            self.draw_everything()
            pg.display.flip()
            pg.display.update()

        pg.quit()
