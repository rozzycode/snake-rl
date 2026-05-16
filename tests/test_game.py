from snake_rl.game import Direction, SnakeGame


def test_snake_moves_one_cell_in_current_direction():
    game = SnakeGame(width=10, height=10)
    start = game.head

    game.step(Direction.RIGHT)

    assert game.head == (start[0] + 1, start[1])


def test_snake_grows_after_eating_food():
    game = SnakeGame(width=10, height=10)
    game.snake = [(5, 5), (4, 5), (3, 5)]
    game.direction = Direction.RIGHT
    game.food = (6, 5)

    game.step(Direction.RIGHT)

    assert len(game.snake) == 4
    assert game.score == 1


def test_collision_with_wall_ends_game():
    game = SnakeGame(width=4, height=4)
    game.snake = [(3, 2), (2, 2), (1, 2)]
    game.direction = Direction.RIGHT

    result = game.step(Direction.RIGHT)

    assert result.done is True
    assert result.ate_food is False


def test_collision_with_body_ends_game():
    game = SnakeGame(width=6, height=6)
    game.snake = [(3, 3), (3, 4), (2, 4), (2, 3), (2, 2), (3, 2)]
    game.direction = Direction.UP

    result = game.step(Direction.LEFT)

    assert result.done is True
    assert result.ate_food is False
