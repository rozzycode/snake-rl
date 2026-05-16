# Snake DQN Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a DQN-based agent, training mode, and watch mode to the existing Snake reinforcement learning project.

**Architecture:** The DQN implementation will coexist with the tabular Q-learning pipeline. It will reuse the existing Snake environment and action space while adding a richer state vector, a PyTorch neural network, replay memory, and a target network.

**Tech Stack:** Python, `uv`, `pygame`, `pytest`, `torch`

---

### Task 1: Add Torch dependency and DQN CLI coverage

**Files:**
- Modify: `pyproject.toml`
- Modify: `src/snake_rl/main.py`
- Test: `tests/test_main.py`

**Step 1: Write the failing test**

Add parser tests for:

- `train-dqn` mode is accepted;
- `watch-dqn` mode is accepted.

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_main.py -v`
Expected: FAIL because the new modes are not registered yet.

**Step 3: Write minimal implementation**

- Add `torch` dependency.
- Extend CLI modes to include `train-dqn` and `watch-dqn`.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_main.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add pyproject.toml src/snake_rl/main.py tests/test_main.py
git commit -m "chore: add dqn cli modes and dependency"
```

### Task 2: Build DQN state extraction and model

**Files:**
- Create: `src/snake_rl/dqn_agent.py`
- Test: `tests/test_dqn_agent.py`

**Step 1: Write the failing test**

Add tests for:

- state vector has stable size;
- network outputs 3 Q-values;
- save/load round trip works.

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_dqn_agent.py -v`
Expected: FAIL because DQN components are missing.

**Step 3: Write minimal implementation**

- Add a simple feed-forward network.
- Add DQN agent wrapper with state-size awareness.
- Add save/load support.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_dqn_agent.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/dqn_agent.py tests/test_dqn_agent.py
git commit -m "feat: add dqn agent core"
```

### Task 3: Add replay buffer and optimization step

**Files:**
- Modify: `src/snake_rl/dqn_agent.py`
- Test: `tests/test_dqn_agent.py`

**Step 1: Write the failing test**

Add tests for:

- replay buffer stores transitions;
- sampled batches have the expected shape;
- optimization step changes model weights.

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_dqn_agent.py -v`
Expected: FAIL because replay and training are incomplete.

**Step 3: Write minimal implementation**

- Add replay memory.
- Add target network.
- Add mini-batch optimization step.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_dqn_agent.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/dqn_agent.py tests/test_dqn_agent.py
git commit -m "feat: add dqn replay and optimization"
```

### Task 4: Implement DQN training pipeline

**Files:**
- Create: `src/snake_rl/dqn_train.py`
- Test: `tests/test_dqn_train.py`

**Step 1: Write the failing test**

Add tests for:

- short DQN training run returns metrics;
- model checkpoint is saved;
- state vector is accepted end to end.

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_dqn_train.py -v`
Expected: FAIL because training pipeline is missing.

**Step 3: Write minimal implementation**

- Build DQN training loop.
- Save `artifacts/dqn_model.pt`.
- Return summary metrics.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_dqn_train.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/dqn_train.py tests/test_dqn_train.py
git commit -m "feat: add dqn training pipeline"
```

### Task 5: Add DQN watch mode integration

**Files:**
- Modify: `src/snake_rl/main.py`
- Modify: `src/snake_rl/render.py`
- Test: `tests/test_main.py`

**Step 1: Write the failing test**

Add parser and smoke tests for:

- `watch-dqn` mode is routed correctly;
- missing model path reports an error.

**Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_main.py -v`
Expected: FAIL because `watch-dqn` behavior is incomplete.

**Step 3: Write minimal implementation**

- Add `watch-dqn` runtime path.
- Load the DQN model.
- Reuse the renderer to play the model visually.

**Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_main.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/snake_rl/main.py src/snake_rl/render.py tests/test_main.py
git commit -m "feat: add dqn watch mode"
```

### Task 6: Final documentation and smoke verification

**Files:**
- Modify: `README.md`

**Step 1: Write the failing test**

Manually verify:

- `uv run python -m snake_rl.main train-dqn`
- `uv run python -m snake_rl.main watch-dqn`

**Step 2: Run test to verify it fails**

Run the commands before final polish.
Expected: at least one usability issue or incomplete behavior remains.

**Step 3: Write minimal implementation**

- Document DQN setup and commands.
- Add model artifact location to README.

**Step 4: Run test to verify it passes**

Run:

- `uv run pytest -v`
- `uv run python -m snake_rl.main train-dqn`
- `uv run python -m snake_rl.main watch-dqn`

Expected: tests pass and DQN modes behave as documented.

**Step 5: Commit**

```bash
git add README.md
git commit -m "docs: document dqn workflow"
```
