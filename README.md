### Snake RL

Coursework project: Snake game in Python with a Q-learning agent.

###### Setup

```bash
uv sync --dev
```

###### Commands

- `uv run python -m snake_rl.main play`
- `uv run python -m snake_rl.main train`
- `uv run python -m snake_rl.main watch`

###### Example training run

```bash
uv run python -m snake_rl.main train --episodes 300
```

The trained Q-table is saved to `artifacts/q_table.pkl`.
