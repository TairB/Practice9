"""
Music Player — интерактивный музыкальный плеер на Pygame.

Управление:
  P — Play / Resume
  S — Stop
  SPACE — Pause/Unpause
  N — Next track
  B — Back (previous)
  Q / ESC — Quit

Для работы положи .wav или .mp3 файлы в папку music/
"""

import pygame
import sys

from player import MusicPlayer


# ─── Константы ────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 600, 400
FPS = 30

# Цвета (используем кортежи RGB)
C_BG       = (15, 15, 25)      # тёмный фон
C_PANEL    = (30, 30, 50)      # панель
C_WHITE    = (240, 240, 255)
C_ACCENT   = (120, 200, 255)   # голубой акцент
C_MUTED    = (100, 100, 130)
C_GREEN    = (80, 200, 120)
C_RED      = (220, 80, 80)
C_YELLOW   = (255, 200, 60)


def draw_ui(screen, fonts, player):
    """
    Рисует весь интерфейс плеера.
    
    Разбиваем на части:
      - фон и панель
      - название трека
      - статус (играет/стоп)
      - позиция воспроизведения
      - прогресс-бар (визуальный)
      - подсказки по клавишам
    """
    font_large, font_medium, font_small = fonts

    # ── Фон ──────────────────────────────────────────────────────────────────
    screen.fill(C_BG)

    # Центральная панель
    panel_rect = pygame.Rect(40, 40, WIDTH - 80, 260)
    pygame.draw.rect(screen, C_PANEL, panel_rect, border_radius=16)
    pygame.draw.rect(screen, C_ACCENT, panel_rect, width=1, border_radius=16)

    # ── Заголовок "🎵 Music Player" ──────────────────────────────────────────
    title_surf = font_large.render("♪ Music Player", True, C_ACCENT)
    screen.blit(title_surf, title_surf.get_rect(centerx=WIDTH // 2, y=55))

    # ── Название трека ────────────────────────────────────────────────────────
    track_name = player.get_track_name()
    # Обрезаем длинное имя
    if len(track_name) > 30:
        track_name = track_name[:27] + "..."
    track_surf = font_medium.render(track_name, True, C_WHITE)
    screen.blit(track_surf, track_surf.get_rect(centerx=WIDTH // 2, y=120))

    # Номер трека в плейлисте
    if player.playlist:
        idx_text = f"{player.current_index + 1} / {len(player.playlist)}"
        idx_surf = font_small.render(idx_text, True, C_MUTED)
        screen.blit(idx_surf, idx_surf.get_rect(centerx=WIDTH // 2, y=150))

    # ── Статус ────────────────────────────────────────────────────────────────
    status = player.get_status()
    # Выбираем цвет по статусу
    if "Играет" in status:
        status_color = C_GREEN
    elif "Пауза" in status:
        status_color = C_YELLOW
    else:
        status_color = C_RED
    status_surf = font_medium.render(status, True, status_color)
    screen.blit(status_surf, status_surf.get_rect(centerx=WIDTH // 2, y=185))

    # ── Позиция воспроизведения ───────────────────────────────────────────────
    pos = player.get_position()
    pos_text = f"{int(pos // 60):02d}:{int(pos % 60):02d}"
    pos_surf = font_small.render(pos_text, True, C_MUTED)
    screen.blit(pos_surf, pos_surf.get_rect(centerx=WIDTH // 2, y=220))

    # ── Визуальный прогресс-бар (анимированный) ───────────────────────────────
    bar_x, bar_y, bar_w, bar_h = 80, 250, WIDTH - 160, 8
    pygame.draw.rect(screen, C_MUTED, (bar_x, bar_y, bar_w, bar_h), border_radius=4)
    if player.is_playing:
        # Анимация: прогресс движется каждые 30 сек (визуальный эффект)
        fill_w = int((pos % 30) / 30 * bar_w)
        pygame.draw.rect(screen, C_ACCENT, (bar_x, bar_y, fill_w, bar_h), border_radius=4)

    # ── Подсказки по клавишам ─────────────────────────────────────────────────
    hints = [
        ("[P] Play", C_GREEN),
        ("[S] Stop", C_RED),
        ("[SPACE] Pause", C_YELLOW),
        ("[N] Next", C_ACCENT),
        ("[B] Back", C_ACCENT),
        ("[Q] Quit", C_MUTED),
    ]

    hint_y = 320
    total_width = 0
    rendered = []
    for text, color in hints:
        surf = font_small.render(text, True, color)
        rendered.append(surf)
        total_width += surf.get_width() + 20

    # Центрируем все подсказки
    start_x = (WIDTH - total_width) // 2
    for surf in rendered:
        screen.blit(surf, (start_x, hint_y))
        start_x += surf.get_width() + 20


def main():
    pygame.init()
    pygame.mixer.init()  # Инициализируем звуковую систему

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player 🎵")

    clock = pygame.time.Clock()

    # Шрифты: (большой, средний, маленький)
    fonts = (
        pygame.font.SysFont("Arial", 28, bold=True),
        pygame.font.SysFont("Arial", 22),
        pygame.font.SysFont("Arial", 16),
    )

    # Создаём плеер
    player = MusicPlayer(music_folder="music")

    # ─── Главный цикл ──────────────────────────────────────────────────────────
    running = True
    while running:

        # 1. Обработка событий клавиатуры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_p:
                    player.play()

                elif event.key == pygame.K_s:
                    player.stop()

                elif event.key == pygame.K_SPACE:
                    player.pause()

                elif event.key == pygame.K_n:
                    player.next_track()

                elif event.key == pygame.K_b:
                    player.prev_track()

        # 2. Рисуем интерфейс
        draw_ui(screen, fonts, player)

        # 3. Обновляем экран
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
