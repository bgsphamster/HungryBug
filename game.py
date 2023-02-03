import time
from snake import *
import sys
import msvcrt

class Game:
    def __init__(self) -> None:
        self.snake = Snake()

    def clear_screen(self):
        sys.stdout.flush()
        print("\033c", end="")

    def write_to_phisical_screen(self):
        self.clear_screen()
        board: list[list[bool]] = [[False for i in range(
            MAX_GAMEBOARD_SIZE)] for j in range(MAX_GAMEBOARD_SIZE)]
        for cell in self.snake.body:
            board[cell[X]][cell[Y]] = True

        for column in board:
            for cell in column:
                if cell:
                    print("[]", end="")
                else:
                    print("  ", end="")
            print("\n", end="")
            sys.stdout.flush()

    def main(self):
        ...
        