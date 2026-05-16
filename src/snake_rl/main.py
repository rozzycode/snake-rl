"""Command-line entry point for Snake RL."""

from __future__ import annotations

import argparse
from pathlib import Path

from snake_rl.config import BOARD_HEIGHT, BOARD_WIDTH, MAX_STEPS_PER_EPISODE, TRAIN_EPISODES
from snake_rl.render import exit_with_message, run_agent_watch, run_manual_game
from snake_rl.train import train_agent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Snake RL", allow_abbrev=False)
    parser.add_argument("mode", choices=["play", "train", "watch"])
    parser.add_argument("--episodes", "--ep", type=int, default=TRAIN_EPISODES)
    parser.add_argument("--width", type=int, default=BOARD_WIDTH)
    parser.add_argument("--height", type=int, default=BOARD_HEIGHT)
    parser.add_argument("--max-steps", type=int, default=MAX_STEPS_PER_EPISODE)
    parser.add_argument("--q-table", type=Path, default=Path("artifacts/q_table.pkl"))
    parser.add_argument("--print-q-table", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.mode == "play":
        run_manual_game(width=args.width, height=args.height)
        return

    if args.mode == "train":
        metrics = train_agent(
            episodes=args.episodes,
            width=args.width,
            height=args.height,
            max_steps=args.max_steps,
            output_path=args.q_table,
        )
        print(
            "Training complete. "
            f"Episodes: {metrics['episodes']}, "
            f"average score: {metrics['average_score']:.2f}, "
            f"best score: {metrics['best_score']}"
        )
        return

    try:
        run_agent_watch(
            q_table_path=args.q_table,
            width=args.width,
            height=args.height,
            print_q_table=args.print_q_table,
        )
    except FileNotFoundError as error:
        exit_with_message(str(error))


if __name__ == "__main__":
    main()
