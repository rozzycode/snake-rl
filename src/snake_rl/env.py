from __future__ import annotations

from enum import IntEnum

from snake_rl.game import Direction, SnakeGame


class RelativeAction(IntEnum):
    STRAIGHT = 0
    TURN_LEFT = 1
    TURN_RIGHT = 2


TURN_LEFT = {
    Direction.UP: Direction.LEFT,
    Direction.LEFT: Direction.DOWN,
    Direction.DOWN: Direction.RIGHT,
    Direction.RIGHT: Direction.UP,
}

TURN_RIGHT = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}


class SnakeEnv:
    def __init__(
        self,
        width: int,
        height: int,
        food_reward: float = 10.0,
        collision_penalty: float = -10.0,
        step_penalty: float = -0.1,
    ) -> None:
        self.game = SnakeGame(width=width, height=height)
        self.food_reward = food_reward
        self.collision_penalty = collision_penalty
        self.step_penalty = step_penalty

    def reset(self) -> tuple[int, ...]:
        self.game.reset()
        return self.get_state()

    def step(self, action: RelativeAction) -> tuple[tuple[int, ...], float, bool, dict[str, bool]]:
        direction = self._resolve_direction(action)
        result = self.game.step(direction)

        if result.done:
            reward = self.collision_penalty
        elif result.ate_food:
            reward = self.food_reward
        else:
            reward = self.step_penalty

        return self.get_state(), float(reward), result.done, {"ate_food": result.ate_food}

    def get_state(self) -> tuple[int, ...]:
        head_x, head_y = self.game.head
        current = self.game.direction
        left_dir = TURN_LEFT[current]
        right_dir = TURN_RIGHT[current]
        food_x, food_y = self.game.food

        return (
            int(self._would_collide(current)),
            int(self._would_collide(left_dir)),
            int(self._would_collide(right_dir)),
            int(current == Direction.UP),
            int(current == Direction.DOWN),
            int(current == Direction.LEFT),
            int(current == Direction.RIGHT),
            int(food_x < head_x),
            int(food_x > head_x),
            int(food_y < head_y),
            int(food_y > head_y),
        )

    def _resolve_direction(self, action: RelativeAction) -> Direction:
        current = self.game.direction
        if action == RelativeAction.STRAIGHT:
            return current
        if action == RelativeAction.TURN_LEFT:
            return TURN_LEFT[current]
        return TURN_RIGHT[current]

    def _would_collide(self, direction: Direction) -> bool:
        dx, dy = direction.value
        next_head = (self.game.head[0] + dx, self.game.head[1] + dy)
        x, y = next_head
        if not (0 <= x < self.game.width and 0 <= y < self.game.height):
            return True
        return next_head in self.game.snake[:-1]
