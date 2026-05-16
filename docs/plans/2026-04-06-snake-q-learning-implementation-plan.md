# Snake Q-Learning Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Python `uv` project with a `pygame` Snake game, manual play mode, `Q-learning` training mode, and trained-agent watch mode.

**Architecture:** The project separates pure game rules, reinforcement-learning environment logic, rendering, and training orchestration. The agent uses a compact discrete state and a tabular Q-function so the training process stays explainable and feasible for a coursework project.

**Tech Stack:** Python, `uv`, `pygame`, `pytest`, `pickle`

---

### Task 1: Scaffold the Python project

**Files:**
- Create: `pyproject.toml`
- Create: `README.md`
- Create: `src/snake_rl/__init__.py`
- Create: `src/snake_rl/main.py`
- Create: `src/snake_rl/config.py`

**Step 1: Write the failing test**

Create `tests/test_imports.py` with:

```python
def test_package_import():
    import snake_rl

    assert snake_rl is not None
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_imports.py -v`
Expected: FAIL because the package and test setup do not exist yet.

**Step 3: Write minimal implementation**

- Add a `pyproject.toml` configured for `uv`.
- Add `pygame` as a runtime dependency.
- Add `pytest` as a development dependency.
- Create the package directory and a minimal `__init__.py`.
- Add a minimal `main.py` with CLI mode parsing placeholder.
- Add `config.py` with initial constants.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_imports.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add pyproject.toml README.md src/snake_rl/__init__.py src/snake_rl/main.py src/snake_rl/config.py tests/test_imports.py
git commit -m "chore: scaffold snake rl project"
```

### Task 2: Implement core Snake game logic

**Files:**
- Create: `src/snake_rl/game.py`
- Test: `tests/test_game.py`

**Step 1: Write the failing test**

Add tests for:

- snake moves one cell in current direction;
- snake grows after eating food;
- collision with wall ends the game;
- collision with body ends the game.

Example:

```python
def test_snake_moves_one_cell():
    game = SnakeGame(width=10, height=10)
    start = game.head

    game.step(Direction.RIGHT)

    assert game.head == (start[0] + 1, start[1])
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_game.py -v`
Expected: FAIL because `SnakeGame` and related structures are not implemented.

**Step 3: Write minimal implementation**

- Create `Direction` enum.
- Create `SnakeGame` class.
- Implement state reset, movement, food spawn, growth, and collision detection.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_game.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/game.py tests/test_game.py
git commit -m "feat: implement core snake game logic"
```

### Task 3: Build the reinforcement-learning environment

**Files:**
- Create: `src/snake_rl/env.py`
- Test: `tests/test_env.py`

**Step 1: Write the failing test**

Add tests for:

- compact state extraction format;
- reward when food is eaten;
- penalty when collision occurs;
- returned step tuple contains next state, reward, done, and info.

Example:

```python
def test_env_returns_compact_state():
    env = SnakeEnv(width=10, height=10)
    state = env.reset()

    assert isinstance(state, tuple)
    assert len(state) > 0
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_env.py -v`
Expected: FAIL because the environment wrapper does not exist.

**Step 3: Write minimal implementation**

- Wrap `SnakeGame` inside `SnakeEnv`.
- Convert relative actions into actual snake turns.
- Implement compact discrete feature extraction.
- Implement reward logic and terminal state handling.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_env.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/env.py tests/test_env.py
git commit -m "feat: add snake reinforcement learning environment"
```

### Task 4: Implement the Q-learning agent

**Files:**
- Create: `src/snake_rl/agent.py`
- Test: `tests/test_agent.py`

**Step 1: Write the failing test**

Add tests for:

- unseen states initialize safely;
- greedy action selection uses the best Q-value;
- update rule changes Q-values correctly;
- save/load preserves learned data.

Example:

```python
def test_agent_updates_q_value():
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.0)
    state = ("s",)
    next_state = ("n",)

    agent.update(state, 0, reward=1.0, next_state=next_state, done=False)

    assert agent.q_table[state][0] != 0.0
```

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_agent.py -v`
Expected: FAIL because the agent is not implemented.

**Step 3: Write minimal implementation**

- Create `QLearningAgent`.
- Store Q-values in a dictionary keyed by state.
- Implement `choose_action`.
- Implement `update`.
- Implement `save` and `load`.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_agent.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/agent.py tests/test_agent.py
git commit -m "feat: implement q-learning agent"
```

### Task 5: Add pygame rendering for manual and watch modes

**Files:**
- Create: `src/snake_rl/render.py`
- Modify: `src/snake_rl/main.py`

**Step 1: Write the failing test**

Add a lightweight test that imports the renderer module and verifies key constants or helper functions are available without starting the game loop.

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_render_import.py -v`
Expected: FAIL because the renderer does not exist.

**Step 3: Write minimal implementation**

- Create a `pygame` renderer for the board, snake, food, and score.
- Add a manual loop for `play`.
- Add a watch loop that loads the trained agent and lets it choose actions.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_render_import.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/render.py src/snake_rl/main.py tests/test_render_import.py
git commit -m "feat: add pygame game rendering modes"
```

### Task 6: Implement the training loop

**Files:**
- Create: `src/snake_rl/train.py`
- Modify: `src/snake_rl/main.py`
- Test: `tests/test_train.py`

**Step 1: Write the failing test**

Add tests for:

- one training episode updates agent state;
- training creates an output file;
- summary metrics are returned.

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_train.py -v`
Expected: FAIL because the training module is not implemented.

**Step 3: Write minimal implementation**

- Implement the episode loop.
- Add epsilon decay.
- Save the Q-table into `artifacts/q_table.pkl`.
- Print or return simple aggregate statistics.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_train.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/train.py src/snake_rl/main.py tests/test_train.py
git commit -m "feat: add q-learning training pipeline"
```

### Task 7: Final integration and documentation

**Files:**
- Modify: `README.md`
- Modify: `src/snake_rl/main.py`

**Step 1: Write the failing test**

Manually verify the CLI scenarios:

- `play` starts a manual game;
- `train` runs training and creates a Q-table;
- `watch` loads the saved Q-table and runs the agent.

**Step 2: Run test to verify it fails**

Run each command before final fixes.
Expected: at least one command or edge case still behaves incorrectly before integration polish.

**Step 3: Write minimal implementation**

- Finalize CLI argument handling.
- Improve user-facing error messages.
- Document setup and commands in `README.md`.

**Step 4: Run test to verify it passes**

Run:

- `uv run pytest -v`
- `uv run python -m snake_rl.main train`
- `uv run python -m snake_rl.main play`
- `uv run python -m snake_rl.main watch`

Expected: tests pass and all modes behave as documented.

**Step 5: Commit**

```bash
git add README.md src/snake_rl/main.py
git commit -m "docs: finalize snake rl usage and integration"
```
