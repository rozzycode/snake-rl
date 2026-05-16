from pathlib import Path


def test_toc_does_not_use_chapter_heading_spacing():
    main_tex = Path(__file__).resolve().parents[1] / "overleaf-sync" / "main.tex"
    content = main_tex.read_text(encoding="utf-8")

    assert r"\chapter*{\large ОГЛАВЛЕНИЕ}" not in content
    assert r"\renewcommand{\contentsname}{\makebox[\textwidth][c]{ОГЛАВЛЕНИЕ}}" in content
    assert r"\renewcommand{\cfttoctitlefont}{\normalsize\bfseries}" in content
    assert r"\setlength{\cftbeforetoctitleskip}{0pt}" in content
    assert r"\setlength{\cftaftertoctitleskip}{0.5\baselineskip}" in content
