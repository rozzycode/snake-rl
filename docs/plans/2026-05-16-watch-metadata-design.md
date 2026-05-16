# Watch Metadata Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a compact training summary to watch mode and a separate CLI flag to print the full Q-table to the console.

**Architecture:** Extend the watch CLI with a boolean flag, compute a small metadata summary from the current config and loaded Q-table, and render that summary in the watch HUD. Keep the full Q-table out of the game window and print it only when the explicit flag is passed.

**Tech Stack:** Python, argparse, pygame, existing Snake RL modules

---

### Task 1: Extend CLI parsing

**Files:**
- Modify: `src/snake_rl/main.py`
- Test: `tests/test_main.py`

**Step 1:** Add a `--print-q-table` flag to the parser.

**Step 2:** Pass the parsed flag into watch mode.

### Task 2: Add watch metadata rendering

**Files:**
- Modify: `src/snake_rl/render.py`

**Step 1:** Build a compact summary string with training and runtime parameters.

**Step 2:** Render the summary as a second HUD line in watch mode.

### Task 3: Print Q-table on demand

**Files:**
- Modify: `src/snake_rl/render.py`

**Step 1:** Add a small helper that prints sorted Q-table rows.

**Step 2:** Invoke it only when the new CLI flag is enabled.

### Task 4: Verify behavior

**Files:**
- Test: `tests/test_main.py`

**Step 1:** Add a parser test for the new flag.

**Step 2:** Run focused tests and CLI help checks.
