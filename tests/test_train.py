from pathlib import Path

from snake_rl.train import train_agent


def test_training_creates_output_file(tmp_path: Path):
    output_path = tmp_path / "q_table.pkl"

    metrics = train_agent(
        episodes=3,
        width=8,
        height=8,
        max_steps=20,
        output_path=output_path,
    )

    assert output_path.exists()
    assert metrics["episodes"] == 3


def test_training_returns_summary_metrics(tmp_path: Path):
    metrics = train_agent(
        episodes=2,
        width=8,
        height=8,
        max_steps=15,
        output_path=tmp_path / "table.pkl",
    )

    assert "average_score" in metrics
    assert "best_score" in metrics
    assert "episodes" in metrics
