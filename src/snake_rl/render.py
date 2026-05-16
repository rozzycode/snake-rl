"""pygame rendering and runtime loops."""

from __future__ import annotations

from pathlib import Path

import pygame

from snake_rl.agent import QLearningAgent
from snake_rl.config import (
    ALPHA,
    BOARD_HEIGHT,
    BOARD_WIDTH,
    CELL_SIZE,
    COLLISION_PENALTY,
    EPSILON_DECAY,
    EPSILON_MIN,
    FPS,
    FOOD_REWARD,
    GAMMA,
    MAX_STEPS_PER_EPISODE,
    STEP_PENALTY,
)
from snake_rl.env import SnakeEnv
from snake_rl.game import Direction, SnakeGame


class Renderer:
    def __init__(self, width: int, height: int, cell_size: int, fps: int, hud_height: int = 40) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.fps = fps
        self.hud_height = hud_height
        self.window_width = width * cell_size
        self.window_height = height * cell_size + hud_height

    def setup(self) -> tuple[pygame.Surface, pygame.time.Clock, pygame.font.Font]:
        pygame.init()
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Snake RL")
        return screen, pygame.time.Clock(), pygame.font.SysFont("arial", 24)

    def draw(
        self,
        screen: pygame.Surface,
        font: pygame.font.Font,
        game: SnakeGame,
        title: str,
        metadata: list[str] | None = None,
    ) -> None:
        screen.fill((24, 28, 32))
        meta_font = pygame.font.SysFont("arial", 16)
        metadata_lines = metadata or []
        board_top = self.hud_height
        board_rect = pygame.Rect(0, board_top, self.width * self.cell_size, self.height * self.cell_size)
        pygame.draw.rect(screen, (34, 39, 46), board_rect)

        food_rect = pygame.Rect(
            game.food[0] * self.cell_size,
            board_top + game.food[1] * self.cell_size,
            self.cell_size,
            self.cell_size,
        )
        pygame.draw.rect(screen, (225, 90, 76), food_rect, border_radius=4)

        for index, (x_pos, y_pos) in enumerate(game.snake):
            color = (100, 210, 122) if index == 0 else (72, 168, 93)
            rect = pygame.Rect(x_pos * self.cell_size, board_top + y_pos * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, color, rect, border_radius=4)

        text = font.render(f"{title} | Score: {game.score}", True, (236, 240, 241))
        screen.blit(text, (12, 8))
        for index, line in enumerate(metadata_lines):
            meta_text = meta_font.render(line, True, (180, 188, 196))
            screen.blit(meta_text, (12, 40 + index * 18))
        pygame.display.flip()

    def get_restart_button_rect(self) -> pygame.Rect:
        modal_width = min(300, self.window_width - 40)
        modal_height = 220
        modal_left = (self.window_width - modal_width) // 2
        modal_top = (self.window_height - modal_height) // 2
        button_width = 180
        button_height = 44
        button_left = modal_left + (modal_width - button_width) // 2
        button_top = modal_top + 144
        return pygame.Rect(button_left, button_top, button_width, button_height)

    def draw_game_over_modal(
        self,
        screen: pygame.Surface,
        font: pygame.font.Font,
        score: int,
        mouse_position: tuple[int, int] | None = None,
    ) -> pygame.Rect:
        overlay = pygame.Surface((self.window_width, self.window_height), pygame.SRCALPHA)
        overlay.fill((10, 12, 16, 170))
        screen.blit(overlay, (0, 0))

        modal_width = min(300, self.window_width - 40)
        modal_height = 220
        modal_left = (self.window_width - modal_width) // 2
        modal_top = (self.window_height - modal_height) // 2
        modal_rect = pygame.Rect(modal_left, modal_top, modal_width, modal_height)
        pygame.draw.rect(screen, (244, 240, 230), modal_rect, border_radius=16)
        pygame.draw.rect(screen, (210, 204, 190), modal_rect, width=2, border_radius=16)

        title = font.render("Проигрыш", True, (41, 44, 51))
        score_text = font.render(f"Счет: {score}", True, (64, 68, 76))
        hint_font = pygame.font.SysFont("arial", 18)
        hint_text = hint_font.render("Нажмите R или кнопку ниже", True, (97, 102, 112))

        screen.blit(title, title.get_rect(center=(self.window_width // 2, modal_top + 46)))
        screen.blit(score_text, score_text.get_rect(center=(self.window_width // 2, modal_top + 92)))
        screen.blit(hint_text, hint_text.get_rect(center=(self.window_width // 2, modal_top + 126)))

        button_rect = self.get_restart_button_rect()
        is_hovered = mouse_position is not None and button_rect.collidepoint(mouse_position)
        button_color = (215, 94, 67) if is_hovered else (195, 82, 58)
        pygame.draw.rect(screen, button_color, button_rect, border_radius=12)
        pygame.draw.rect(screen, (150, 58, 40), button_rect, width=2, border_radius=12)

        button_text = font.render("Перезапустить", True, (255, 249, 245))
        screen.blit(button_text, button_text.get_rect(center=button_rect.center))
        pygame.display.flip()
        return button_rect


def _handle_game_over_modal(
    screen: pygame.Surface,
    clock: pygame.time.Clock,
    font: pygame.font.Font,
    renderer: Renderer,
    score: int,
) -> bool | None:
    while True:
        mouse_position = pygame.mouse.get_pos()
        button_rect = renderer.draw_game_over_modal(screen, font, score, mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    return True

        clock.tick(renderer.fps)


def run_manual_game(
    width: int = BOARD_WIDTH,
    height: int = BOARD_HEIGHT,
    cell_size: int = CELL_SIZE,
    fps: int = FPS,
) -> None:
    renderer = Renderer(width=width, height=height, cell_size=cell_size, fps=fps)
    screen, clock, font = renderer.setup()
    key_to_direction = {
        pygame.K_UP: Direction.UP,
        pygame.K_DOWN: Direction.DOWN,
        pygame.K_LEFT: Direction.LEFT,
        pygame.K_RIGHT: Direction.RIGHT,
    }

    running = True
    while running:
        game = SnakeGame(width=width, height=height)
        current_direction = game.direction
        restart_requested = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        while running and not restart_requested:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key in key_to_direction:
                    current_direction = key_to_direction[event.key]

            if not running:
                break

            result = game.step(current_direction)
            renderer.draw(screen, font, game, "Режим ручной")
            if result.done:
                modal_result = _handle_game_over_modal(screen, clock, font, renderer, game.score)
                if modal_result is None:
                    running = False
                else:
                    restart_requested = True
                break
            clock.tick(fps)

    pygame.quit()


def run_agent_watch(
    q_table_path: Path,
    width: int = BOARD_WIDTH,
    height: int = BOARD_HEIGHT,
    cell_size: int = CELL_SIZE,
    fps: int = FPS,
    print_q_table: bool = False,
) -> None:
    if not q_table_path.exists():
        raise FileNotFoundError(f"Trained Q-table not found: {q_table_path}")

    agent = QLearningAgent.load(q_table_path, alpha=ALPHA, gamma=GAMMA, epsilon=0.0)
    metadata = _build_watch_metadata(width=width, height=height, fps=fps, q_table_size=len(agent.q_table))
    hud_height = _get_watch_hud_height(metadata)
    renderer = Renderer(width=width, height=height, cell_size=cell_size, fps=fps, hud_height=hud_height)
    screen, clock, font = renderer.setup()

    if print_q_table:
        _print_q_table(agent)

    running = True
    while running:
        env = SnakeEnv(width=width, height=height)
        state = env.reset()
        restart_requested = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        while running and not restart_requested:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not running:
                break

            action = agent.choose_action(state)
            state, _, done, _ = env.step(action)
            renderer.draw(screen, font, env.game, "Режим агента", metadata=metadata)
            if done:
                modal_result = _handle_game_over_modal(screen, clock, font, renderer, env.game.score)
                if modal_result is None:
                    running = False
                else:
                    restart_requested = True
                break
            clock.tick(fps)

    pygame.quit()


def exit_with_message(message: str, exit_code: int = 1) -> None:
    print(message)
    raise SystemExit(exit_code)


def _build_watch_metadata(width: int, height: int, fps: int, q_table_size: int) -> list[str]:
    return [
        f"board: {width}x{height}",
        f"fps: {fps}",
        f"alpha: {ALPHA}",
        f"gamma: {GAMMA}",
        f"eps_min: {EPSILON_MIN}",
        f"eps_decay: {EPSILON_DECAY}",
        f"max_steps: {MAX_STEPS_PER_EPISODE}",
        f"q_states: {q_table_size}",
        f"food_reward: {FOOD_REWARD}",
        f"collision_penalty: {COLLISION_PENALTY}",
        f"step_penalty: {STEP_PENALTY}",
    ]


def _get_watch_hud_height(metadata: list[str]) -> int:
    if not metadata:
        return 40
    return 40 + (len(metadata) * 18) + 12


def _print_q_table(agent: QLearningAgent) -> None:
    print("Loaded Q-table:")
    for state in sorted(agent.q_table):
        q_values = ", ".join(f"{value:.4f}" for value in agent.q_table[state])
        print(f"{state}: [{q_values}]")
