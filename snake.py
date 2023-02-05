from enum import Enum
import food

class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


MAX_GAMEBOARD_SIZE = 10
X = 0
Y = 1


class InvalidMovingError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Snake:
    def __init__(self) -> None:
        self.body: list[tuple[int, int]] = [(0, 0)]

    def move(self, direction: Direction) -> None:
        next = {
            Direction.RIGHT: (self.body[0][X], self.body[0][Y]+1),
            Direction.LEFT: (self.body[0][X], self.body[0][Y]-1),
            Direction.UP: (self.body[0][X]-1, self.body[0][Y]),
            Direction.DOWN: (self.body[0][X]+1, self.body[0][Y])
        }[direction]
        # 先验证新位置合法性，要求不是身体的一部分，不超过边界
        if MAX_GAMEBOARD_SIZE >= next[X] >= 0 and MAX_GAMEBOARD_SIZE >= next[Y] >= 0 and self.body.count(next) == 0:
            # 把最后一节身体移到移动的目标位置，形成新的蛇头
            self.body.pop()
            self.body.insert(0, next)
            
            # 如果是食物，吃
            if(next == food.food_position):
                self.eat(direction)
            return
        raise InvalidMovingError("Invalid moving")

    def eat(self, where: Direction) -> None:
        next = {
            Direction.DOWN: (self.body[0][X], self.body[0][Y]+1),
            Direction.UP: (self.body[0][X], self.body[0][Y]-1),
            Direction.LEFT: (self.body[0][X]-1, self.body[0][Y]),
            Direction.RIGHT: (self.body[0][X]+1, self.body[0][Y])
        }[where]
        self.body.insert(0, next)
        food.food_position = __import__("game").gen_random_food_position(self)