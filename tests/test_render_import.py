from snake_rl.render import Renderer


def test_renderer_exposes_dimensions():
    renderer = Renderer(width=20, height=20, cell_size=24, fps=10)

    assert renderer.window_width == 480
    assert renderer.window_height == 520


def test_renderer_restart_button_rect_is_inside_window():
    renderer = Renderer(width=20, height=20, cell_size=24, fps=10)

    rect = renderer.get_restart_button_rect()

    assert rect.width > 0
    assert rect.height > 0
    assert 0 <= rect.left < renderer.window_width
    assert 0 <= rect.top < renderer.window_height
