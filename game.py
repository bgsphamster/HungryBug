import time
from snake import *
import sys
import msvcrt
import random
import food
import console_colorer


def gen_random_food_position(s: Snake) -> tuple[int, int]:
    ans = (114514, 114514)
    while True:
        ans = (random.randint(0, MAX_GAMEBOARD_SIZE) % MAX_GAMEBOARD_SIZE,
               random.randint(0, MAX_GAMEBOARD_SIZE) % MAX_GAMEBOARD_SIZE)
        if s.body.count(ans) > 0:
            continue
        return ans


class Game:
    def __init__(self) -> None:
        self.snake = Snake()
        food.food_position = gen_random_food_position(self.snake)

    def clear_screen(self):
        print("\033c", end="")

    def write_to_physical_screen(self):
        self.clear_screen()
        board: list[list[bool]] = [[False for i in range(
            MAX_GAMEBOARD_SIZE)] for j in range(MAX_GAMEBOARD_SIZE)]
        for cell in self.snake.body:
            board[cell[X]][cell[Y]] = True

        for i in range(len(board)):
            for j in range(len(board[i])):
                if food.food_position == (i, j):
                    console_colorer.printRed("[]")
                if board[i][j]:
                    print("[]", end="")
                else:
                    print("  ", end="")
            print("\n", end="", flush=True)

    def show_death(self):
        self.clear_screen()
        print("你死了！")
        print("按 y 重新开始，其他键退出")
        opr = msvcrt.getch().decode().lower()
        if opr == 'y':
            self.__init__()
            self.main()
        else:
            sys.exit(0)

    def main(self):
        self.clear_screen()
        print("贪吃蛇（Python console windows v0.1）")
        print("按任意键开始")
        msvcrt.getch()
        self.clear_screen()
        # 主循环
        try:
            while True:
                self.write_to_physical_screen()
                opr = msvcrt.getch().decode().lower()
                match opr:
                    case 'w':
                        self.snake.move(Direction.UP)
                    case 'a':
                        self.snake.move(Direction.LEFT)
                    case 's':
                        self.snake.move(Direction.DOWN)
                    case 'd':
                        self.snake.move(Direction.RIGHT)
        except Exception:
            self.show_death()
        # except InvalidMovingError:
        #     self.show_death()
