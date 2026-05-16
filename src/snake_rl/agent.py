"""Q-learning agent implementation."""

from __future__ import annotations

from pathlib import Path
import pickle
import random


class QLearningAgent:
    def __init__(self, alpha: float, gamma: float, epsilon: float, action_size: int = 3) -> None:
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.action_size = action_size
        self.q_table: dict[tuple[int, ...] | tuple[str, ...], list[float]] = {}
        self.random = random.Random()

    def get_q_values(self, state: tuple[int, ...] | tuple[str, ...]) -> list[float]:
        if state not in self.q_table:
            self.q_table[state] = [0.0] * self.action_size
        return self.q_table[state]

    def choose_action(self, state: tuple[int, ...] | tuple[str, ...]) -> int:
        if self.random.random() < self.epsilon:
            return self.random.randrange(self.action_size)

        q_values = self.get_q_values(state)
        best_value = max(q_values)
        for index, value in enumerate(q_values):
            if value == best_value:
                return index
        return 0

    def update(
        self,
        state: tuple[int, ...] | tuple[str, ...],
        action: int,
        reward: float,
        next_state: tuple[int, ...] | tuple[str, ...],
        done: bool,
    ) -> None:
        current_q = self.get_q_values(state)[action]
        next_best = 0.0 if done else max(self.get_q_values(next_state))
        target = reward + (self.gamma * next_best)
        self.q_table[state][action] = current_q + self.alpha * (target - current_q)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as file_obj:
            pickle.dump(self.q_table, file_obj)

    @classmethod
    def load(
        cls,
        path: Path,
        alpha: float,
        gamma: float,
        epsilon: float,
        action_size: int = 3,
    ) -> "QLearningAgent":
        agent = cls(alpha=alpha, gamma=gamma, epsilon=epsilon, action_size=action_size)
        with path.open("rb") as file_obj:
            agent.q_table = pickle.load(file_obj)
        return agent
