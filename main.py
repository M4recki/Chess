from pieces import Pawn, Rook, Bishop, Knight, Queen, King
from game_logic import GameLogic

def main():
    game = GameLogic()

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
            game.piece_manager.add_figure(figure_type, pos, 7, "white")
            game.piece_manager.add_figure(figure_type, pos, 0, "black")

    # Add pawns
    for x_cell in range(8):
        game.piece_manager.add_figure("Pawn", x_cell, 6, "white")
        game.piece_manager.add_figure("Pawn", x_cell, 1, "black")

    game.run()

if __name__ == "__main__":
    main()
