"""
Moving Ball — красный мяч, управляемый стрелками.

Управление:
  ← ↑ → ↓  — движение мяча (20px за нажатие)
  R         — сбросить в центр
  Q / ESC   — выход
"""

import pygame
import sys

from ball import Ball


# ─── Константы ────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 600, 500
FPS = 60
BG_COLOR = (255, 255, 255)      # белый фон (по условию задания)
TEXT_COLOR = (80, 80, 80)
GRID_COLOR = (230, 230, 230)    # цвет сетки


def draw_grid(screen):
    """Рисует лёгкую сетку для ориентира."""
    for x in range(0, WIDTH, 50):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 50):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))


def draw_info(screen, font, ball):
    """Отображает координаты мяча и подсказки."""
    x, y = ball.get_position()

    # Координаты мяча
    coord_text = f"Позиция: ({x}, {y})"
    coord_surf = font.render(coord_text, True, TEXT_COLOR)
    screen.blit(coord_surf, (10, 10))

    # Подсказки
    hints = "← ↑ → ↓ Двигать  |  R Сброс  |  Q Выход"
    hint_surf = font.render(hints, True, TEXT_COLOR)
    screen.blit(hint_surf, (10, HEIGHT - 30))


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball 🔴")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    # Создаём мяч в центре экрана
    ball = Ball(WIDTH, HEIGHT)

    # ─── Главный цикл ──────────────────────────────────────────────────────────
    running = True
    while running:

        # 1. Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # Управление мячом — стрелки
                if event.key == pygame.K_UP:
                    ball.move('up')
                elif event.key == pygame.K_DOWN:
                    ball.move('down')
                elif event.key == pygame.K_LEFT:
                    ball.move('left')
                elif event.key == pygame.K_RIGHT:
                    ball.move('right')

                # Дополнительные клавиши
                elif event.key == pygame.K_r:
                    # Сброс в центр
                    ball = Ball(WIDTH, HEIGHT)

                elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False

        # 2. Рисуем фон (белый)
        screen.fill(BG_COLOR)

        # 3. Сетка (опционально, для наглядности)
        draw_grid(screen)

        # 4. Рисуем мяч
        ball.draw(screen)

        # 5. Информация на экране
        draw_info(screen, font, ball)

        # 6. Обновляем дисплей
        pygame.display.flip()

        # 7. Ограничиваем FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
