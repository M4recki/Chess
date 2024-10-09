import pygame as pg

class Board:
    def __init__(self):
        self.screen = pg.display.set_mode((600, 600))
        self.clock = pg.time.Clock()
        self.running = True
        self.board_image = pg.image.load("assets/images/board.png")
        self.board_image = pg.transform.scale(self.board_image, (600, 600))
        self.title = pg.display.set_caption("Chess by Marek B")
        self.icon = pg.image.load("assets/images/chess_icon.png")
        self.set_icon = pg.display.set_icon(self.icon)

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.blit(self.board_image, (0, 0))

            pg.display.flip()
            pg.display.update()

        pg.quit()
