from __future__ import annotations

from pathlib import Path

from snake_rl.agent import QLearningAgent
from snake_rl.config import (
    ALPHA,
    BOARD_HEIGHT,
    BOARD_WIDTH,
    COLLISION_PENALTY,
    EPSILON,
    EPSILON_DECAY,
    EPSILON_MIN,
    FOOD_REWARD,
    GAMMA,
    MAX_STEPS_PER_EPISODE,
    STEP_PENALTY,
    TRAIN_EPISODES,
)
from snake_rl.env import SnakeEnv


def build_env(width: int = BOARD_WIDTH, height: int = BOARD_HEIGHT) -> SnakeEnv:
    return SnakeEnv(
        width=width,
        height=height,
        food_reward=FOOD_REWARD,
        collision_penalty=COLLISION_PENALTY,
        step_penalty=STEP_PENALTY,
    )


def build_agent(epsilon: float = EPSILON) -> QLearningAgent:
    return QLearningAgent(alpha=ALPHA, gamma=GAMMA, epsilon=epsilon)


def train_agent(
    episodes: int = TRAIN_EPISODES,
    width: int = BOARD_WIDTH,
    height: int = BOARD_HEIGHT,
    max_steps: int = MAX_STEPS_PER_EPISODE,
    output_path: Path = Path("artifacts/q_table.pkl"),
) -> dict[str, float | int]:
    env = build_env(width=width, height=height)
    agent = build_agent()
    scores: list[int] = []

    for _ in range(episodes):
        state = env.reset()
        for _ in range(max_steps):
            action = agent.choose_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.update(state, action, reward, next_state, done)
            state = next_state
            if done:
                break

        scores.append(env.game.score)
        agent.epsilon = max(EPSILON_MIN, agent.epsilon * EPSILON_DECAY)

    agent.save(output_path)

    average_score = sum(scores) / len(scores) if scores else 0.0
    best_score = max(scores) if scores else 0
    return {
        "episodes": episodes,
        "average_score": average_score,
        "best_score": best_score,
    }
