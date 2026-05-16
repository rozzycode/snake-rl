from pathlib import Path

from snake_rl.agent import QLearningAgent


def test_unseen_state_is_initialized_with_zero_values():
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.0)

    values = agent.get_q_values(("state",))

    assert values == [0.0, 0.0, 0.0]


def test_greedy_action_selection_uses_best_q_value():
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.0)
    state = ("state",)
    agent.q_table[state] = [1.0, 3.0, 2.0]

    action = agent.choose_action(state)

    assert action == 1


def test_agent_updates_q_value():
    agent = QLearningAgent(alpha=0.5, gamma=0.9, epsilon=0.0)
    state = ("s",)
    next_state = ("n",)

    agent.update(state, 0, reward=1.0, next_state=next_state, done=False)

    assert agent.q_table[state][0] == 0.5


def test_save_and_load_preserve_q_table(tmp_path: Path):
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.0)
    agent.q_table[("state",)] = [1.0, 2.0, 3.0]
    path = tmp_path / "q_table.pkl"

    agent.save(path)
    loaded = QLearningAgent.load(path, alpha=0.1, gamma=0.9, epsilon=0.0)

    assert loaded.q_table == agent.q_table
