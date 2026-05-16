from snake_rl.env import RelativeAction, SnakeEnv
from snake_rl.game import Direction


def test_env_returns_compact_state():
    env = SnakeEnv(width=10, height=10)

    state = env.reset()

    assert isinstance(state, tuple)
    assert len(state) == 11


def test_env_rewards_food():
    env = SnakeEnv(width=10, height=10)
    env.reset()
    env.game.snake = [(5, 5), (4, 5), (3, 5)]
    env.game.direction = Direction.RIGHT
    env.game.food = (6, 5)

    _, reward, done, info = env.step(RelativeAction.STRAIGHT)

    assert reward == env.food_reward
    assert done is False
    assert info["ate_food"] is True


def test_env_penalizes_collision():
    env = SnakeEnv(width=4, height=4)
    env.reset()
    env.game.snake = [(3, 2), (2, 2), (1, 2)]
    env.game.direction = Direction.RIGHT

    _, reward, done, info = env.step(RelativeAction.STRAIGHT)

    assert reward == env.collision_penalty
    assert done is True
    assert info["ate_food"] is False


def test_env_step_returns_next_state_reward_done_and_info():
    env = SnakeEnv(width=10, height=10)
    env.reset()

    next_state, reward, done, info = env.step(RelativeAction.STRAIGHT)

    assert isinstance(next_state, tuple)
    assert isinstance(reward, float)
    assert isinstance(done, bool)
    assert isinstance(info, dict)
