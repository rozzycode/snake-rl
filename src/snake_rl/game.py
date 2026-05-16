"""Core Snake game logic."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import random


Position = tuple[int, int]


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


@dataclass(frozen=True)
class StepResult:
    done: bool
    ate_food: bool


class SnakeGame:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.random = random.Random()
        self.reset()

    def reset(self) -> None:
        center = (self.width // 2, self.height // 2)
        self.snake: list[Position] = [
            center,
            (center[0] - 1, center[1]),
            (center[0] - 2, center[1]),
        ]
        self.direction = Direction.RIGHT
        self.score = 0
        self.game_over = False
        self.food = self._spawn_food()

    @property
    def head(self) -> Position:
        return self.snake[0]

    def step(self, direction: Direction | None = None) -> StepResult:
        if self.game_over:
            return StepResult(done=True, ate_food=False)

        next_direction = direction or self.direction
        if self._is_opposite(next_direction):
            next_direction = self.direction
        self.direction = next_direction

        dx, dy = self.direction.value
        next_head = (self.head[0] + dx, self.head[1] + dy)

        hit_wall = not (0 <= next_head[0] < self.width and 0 <= next_head[1] < self.height)
        hit_body = next_head in self.snake[:-1]
        if hit_wall or hit_body:
            self.game_over = True
            return StepResult(done=True, ate_food=False)

        ate_food = next_head == self.food
        self.snake.insert(0, next_head)
        if ate_food:
            self.score += 1
            self.food = self._spawn_food()
        else:
            self.snake.pop()

        return StepResult(done=False, ate_food=ate_food)

    def _spawn_food(self) -> Position:
        free_cells = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
            if (x, y) not in self.snake
        ]
        return self.random.choice(free_cells)

    def _is_opposite(self, direction: Direction) -> bool:
        dx, dy = self.direction.value
        ndx, ndy = direction.value
        return (dx + ndx, dy + ndy) == (0, 0)
