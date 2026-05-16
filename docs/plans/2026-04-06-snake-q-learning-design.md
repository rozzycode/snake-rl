# Snake Q-Learning Design

**Topic:** Reinforcement learning for the Snake game

**Goal:** Build a Python project for the coursework that includes the Snake game on `pygame`, a `Q-learning` agent for automated control, a training mode, a manual play mode, and an agent demonstration mode.

## Scope

The project will focus on the software core of the coursework:

- a playable Snake game;
- a training environment for reinforcement learning;
- a `Q-learning` agent with a tabular state-action value function;
- saving and loading the trained agent;
- a visual demonstration of the trained agent.

The text of the coursework and report materials are out of scope for now.

## Technology Choices

- Language: Python
- Package and environment manager: `uv`
- Graphics and input: `pygame`
- Data persistence: Python standard library serialization (`pickle`)

## Why Q-learning

`Q-learning` is selected as the primary reinforcement learning method because it is:

- simpler to implement than neural approaches such as `DQN`;
- easier to explain in a coursework defense;
- fast enough for a compact state representation;
- suitable for demonstrating the impact of rewards, exploration, and training episodes.

## User Modes

The project will provide three execution modes:

1. `play` — manual game mode for a human player.
2. `train` — training mode for the `Q-learning` agent.
3. `watch` — visual demonstration of a trained agent.

The user explicitly requested two end-user modes: manual play and trained-agent demonstration. Training remains a separate technical mode required to obtain the agent.

## Architecture

The project will separate game logic, environment logic, rendering, and agent logic.

### Main layers

- `game`: pure Snake rules and board updates;
- `env`: reinforcement-learning wrapper around the game;
- `agent`: `Q-learning` policy, Q-table, exploration, and updates;
- `render`: `pygame` drawing and optional HUD;
- `train`: training loop and statistics collection;
- `main`: command entry point and mode selection.

This separation keeps the training logic independent from the graphical interface and makes the project easier to explain and extend later.

## State Representation

The agent will use a compact discrete state instead of the full board.

### Features

- danger straight ahead;
- danger on the left;
- danger on the right;
- current movement direction: `up`, `down`, `left`, `right`;
- food relative to the snake head: `left`, `right`, `up`, `down`.

This representation is intentionally small so that tabular `Q-learning` remains practical.

## Action Space

The agent will have three relative actions:

- `straight`;
- `turn_left`;
- `turn_right`.

Relative actions are preferred over absolute directions because they map naturally to the snake's current heading and reduce invalid command handling.

## Reward Design

Initial reward scheme:

- `+10` for eating food;
- `-10` for collision and game over;
- `-0.1` for each regular step.

This gives the agent a clear positive objective, a strong penalty for failure, and a mild pressure to avoid endless loops.

## Training Strategy

The agent will use `epsilon-greedy` exploration:

- early training: more random exploration;
- later training: more exploitation of learned Q-values.

The Q-table will be updated after every step using the standard `Q-learning` update rule.

Training output will include:

- episode score;
- optional moving average score;
- persisted Q-table saved to `artifacts/q_table.pkl`.

## Proposed Project Structure

```text
coursework/
  pyproject.toml
  README.md
  docs/
    plans/
      2026-04-06-snake-q-learning-design.md
      2026-04-06-snake-q-learning-implementation-plan.md
  artifacts/
  src/
    snake_rl/
      __init__.py
      main.py
      config.py
      game.py
      env.py
      agent.py
      render.py
      train.py
```

## Execution Scenarios

Planned commands:

- `uv run python -m snake_rl.main play`
- `uv run python -m snake_rl.main train`
- `uv run python -m snake_rl.main watch`

## Error Handling and Constraints

- If no trained Q-table exists, `watch` should fail with a clear message.
- Manual and agent modes should use the same game rules.
- Rendering should stay optional for training to avoid unnecessary slowdown.
- Configuration values should be centralized for easier tuning.

## Testing Strategy

The implementation should prioritize lightweight automated tests for logic that does not require a graphical window:

- snake movement and collision handling;
- food spawning constraints;
- state extraction from the environment;
- Q-value updates in the agent;
- save/load behavior for the Q-table.

Rendering behavior can be validated manually during runtime.

## Future Extensions

Possible later improvements:

- training charts export;
- richer reward shaping;
- more advanced state representation;
- comparison with `DQN` as a future development direction in the coursework.
