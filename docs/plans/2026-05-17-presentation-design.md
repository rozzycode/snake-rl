# Presentation Design: RL Snake Coursework

## Context

Coursework topic: "Обучение с подкреплением для игры «Змейка»"
Author: Полегина Александра Дмитриевича, 3rd year, BSU
Format: LaTeX Beamer
Language: Russian
Include: all visuals (screenshots, architecture diagram, tables, training chart)

## Design Principles

- 20% task/problem statement, 80% what was done
- Readable from distance: minimal text, large fonts/graphics
- No tangential information

## Slide Structure (12 slides)

### Section 1: Problem Statement (~20%, 2 slides)

| # | Title | Content |
|---|-------|---------|
| 1 | Title slide | Title, author, supervisor, BSU, 2026 |
| 2 | Task & relevance | Goal + 3-4 task bullets. Why Snake+RL: discrete, few actions, observable result |

### Section 2: What & How (~80%, 10 slides)

| # | Title | Content |
|---|-------|---------|
| 3 | Approach comparison | Table: 4 approaches (rules, path search, Q-learning, DQN), 3 columns. Highlight Q-learning |
| 4 | Agent state | 11 binary features vector — visual diagram (danger/direction/food). Key point: compact yet informative |
| 5 | Actions & reward | 3 relative actions + 3 reward values (10/-10/-0.1). One line: why relative |
| 6 | Architecture | architecture.jpg — 6 modules, connections |
| 7 | Q-learning algorithm | Q-update formula (one large formula) + epsilon-greedy. Minimal text |
| 8 | Interface screenshots | manual_game.jpg, agent_mode.jpg, game_over_modal.jpg |
| 9 | Experiment setup | 5 runs x 8 variants x 100 tests. Brief, large text |
| 10 | Results — chart | learning_chart.jpg — main visual argument |
| 11 | Results — table | Episodes/score table. Highlight growth 4.26 -> 16.23 |
| 12 | Conclusions | 3-4 bullets: goal achieved, Q-learning works, feature limitations, future (DQN) |

## Visual Assets

- `images/architecture.jpg` — module diagram
- `images/manual_game.jpg` — manual mode screenshot
- `images/agent_mode.jpg` — agent mode screenshot
- `images/game_over_modal.jpg` — game over modal
- `images/learning_chart.jpg` — training results chart
- `images/github_qr.png` — GitHub QR (optional)

## Key Data Points

- Average score: 4.262 (50 ep) -> 16.230 (1200 ep)
- Best average score: 15.800 -> 21.600
- State: 11 binary features
- Actions: 3 relative (straight, left, right)
- Reward: +10 (food), -10 (collision), -0.1 (step)
- Hyperparams: alpha=0.1, gamma=0.9, epsilon=1.0->0.05, decay=0.995