# Snake DQN Design

**Topic:** Deep Q-Network extension for the Snake coursework project

**Goal:** Add a second reinforcement learning approach based on `DQN` to the existing Snake project, while preserving the current tabular `Q-learning` pipeline for comparison.

## Scope

This extension adds a neural-network-based agent and training pipeline:

- `DQN` agent for Snake;
- richer state representation than the current tabular setup;
- separate training and watch modes;
- persistence of trained neural-network weights.

The existing `Q-learning` implementation remains in place.

## Why DQN

The current tabular `Q-learning` agent uses a compact state and does not fully account for the snake's changing size and spatial layout. `DQN` is introduced to better model:

- snake length;
- position of the head and food;
- occupancy around the snake;
- broader spatial context relevant for avoiding traps.

## Strategy

`DQN` will be added as a second independent mode rather than replacing `Q-learning`.

### Benefits of this approach

- no regression risk for the already working tabular version;
- direct comparison between `Q-learning` and `DQN` in the coursework;
- easier experimentation and fallback if the neural version requires tuning.

## State Representation

The `DQN` agent will use a vector of engineered features rather than the full board matrix.

### Planned features

- danger straight ahead;
- danger on the left;
- danger on the right;
- current direction: `up`, `down`, `left`, `right`;
- food relative to the head: `left`, `right`, `up`, `down`;
- normalized head coordinates;
- normalized distances to walls;
- snake length;
- fraction of occupied board cells;
- body presence in nearby directions.

This approach provides richer spatial information without the complexity of a full convolutional board model.

## Action Space

The action space remains unchanged:

- `straight`;
- `turn_left`;
- `turn_right`.

This keeps compatibility with the current game environment and simplifies integration.

## DQN Architecture

The neural-network design will stay intentionally compact:

- input layer sized to the state vector;
- 2 fully connected hidden layers;
- output layer with 3 Q-values.

This is sufficient for the coursework scale and avoids overcomplicating training.

## Training Strategy

The `DQN` pipeline will include:

- `epsilon-greedy` exploration;
- replay buffer;
- mini-batch training;
- target network for stabilization;
- periodic model checkpoint saving.

## Rewards

Initial reward shaping remains close to the current setup:

- `+10` for eating food;
- `-10` for collision and game over;
- small negative reward for each regular step.

Later tuning can add shaped rewards such as movement toward food if needed.

## Dependencies

New dependency:

- `torch`

## Project Structure

Planned additions:

```text
src/snake_rl/
  dqn_agent.py
  dqn_train.py
```

Possible light modifications:

- `main.py`
- `env.py`
- `README.md`
- `config.py`

Artifacts:

```text
artifacts/
  dqn_model.pt
```

## CLI Additions

Planned new modes:

- `train-dqn`
- `watch-dqn`

The existing modes stay available:

- `play`
- `train`
- `watch`

## Error Handling

- `watch-dqn` should show a clear error if the model file is missing.
- Training should save the model even if learning progress is modest.
- State-vector construction should remain deterministic and testable.

## Testing Strategy

Add focused tests for:

- DQN state vector shape;
- replay buffer behavior;
- network output dimensions;
- model save/load;
- short smoke training run.

## Expected Coursework Value

With both `Q-learning` and `DQN`, the project can compare:

- explainability versus capacity;
- training speed versus final policy quality;
- limitations of tabular methods for larger spatial reasoning tasks.
