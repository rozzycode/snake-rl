from snake_rl.main import build_parser


def test_parser_accepts_short_episode_flag():
    parser = build_parser()

    args = parser.parse_args(["train", "--ep", "123"])

    assert args.episodes == 123


def test_parser_accepts_print_q_table_flag():
    parser = build_parser()

    args = parser.parse_args(["watch", "--print-q-table"])

    assert args.print_q_table is True
