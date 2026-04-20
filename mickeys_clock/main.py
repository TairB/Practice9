"""
  Q / ESC — выход
"""

import pygame
import sys
import datetime
import os

from clock import MickeyClock


# ─── Константы ────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 500, 500
FPS = 30
BG_COLOR = (245, 245, 220)  # бежевый фон
CENTER = (WIDTH // 2, HEIGHT // 2)


def draw_clock_face(screen, center, radius=180):

   
    pygame.draw.circle(screen, (80, 60, 40), center, radius, 4)

    import math
    for i in range(12):
        angle = math.radians(i * 30 - 90)  # -90 чтобы начать сверху
        x_out = center[0] + int(radius * math.cos(angle))
        y_out = center[1] + int(radius * math.sin(angle))
        x_in  = center[0] + int((radius - 15) * math.cos(angle))
        y_in  = center[1] + int((radius - 15) * math.sin(angle))
        pygame.draw.line(screen, (80, 60, 40), (x_in, y_in), (x_out, y_out), 3)


def draw_time_text(screen, font, minutes, seconds):
    
    text = f"{minutes:02d}:{seconds:02d}"
    surface = font.render(text, True, (50, 30, 10))
    rect = surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(surface, rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock 🕐")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 36, bold=True)

    hand_path = os.path.join("images", "mickey_hand.png")

    if not os.path.exists(hand_path):
        os.makedirs("images", exist_ok=True)
        hand_surface = pygame.Surface((40, 120), pygame.SRCALPHA)
        pygame.draw.rect(hand_surface, (255, 220, 150), (10, 20, 20, 80))
        pygame.draw.circle(hand_surface, (255, 220, 150), (20, 15), 15)
        pygame.image.save(hand_surface, hand_path)
        print(f"[INFO] Создана заглушка руки: {hand_path}")
        print("[INFO] Замените её на настоящий mickey_hand.png")

    mickey_clock = MickeyClock(screen, CENTER, hand_path)

    
    running = True
    while running:

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False

       
        screen.fill(BG_COLOR)

     
        draw_clock_face(screen, CENTER)

       
        minutes, seconds = mickey_clock.draw()

       
        draw_time_text(screen, font, minutes, seconds)

       
        pygame.display.flip()

       
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
