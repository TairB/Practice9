import pygame
import sys

from ball import Ball


WIDTH, HEIGHT = 600, 500
FPS = 60
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (80, 80, 80)
GRID_COLOR = (230, 230, 230)


def draw_grid(screen):
    for x in range(0, WIDTH, 50):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 50):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))


def draw_info(screen, font, ball):
    x, y = ball.get_position()

    coord_text = f"Позиция: ({x}, {y})"
    coord_surf = font.render(coord_text, True, TEXT_COLOR)
    screen.blit(coord_surf, (10, 10))

    hints = "← ↑ → ↓ Двигать  |  R Сброс  |  Q Выход"
    hint_surf = font.render(hints, True, TEXT_COLOR)
    screen.blit(hint_surf, (10, HEIGHT - 30))


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball 🔴")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    ball = Ball(WIDTH, HEIGHT)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move('up')
                elif event.key == pygame.K_DOWN:
                    ball.move('down')
                elif event.key == pygame.K_LEFT:
                    ball.move('left')
                elif event.key == pygame.K_RIGHT:
                    ball.move('right')
                elif event.key == pygame.K_r:
                    ball = Ball(WIDTH, HEIGHT)
                elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False

        screen.fill(BG_COLOR)

        draw_grid(screen)

        ball.draw(screen)

        draw_info(screen, font, ball)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()