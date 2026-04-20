import pygame
import sys

from player import MusicPlayer


WIDTH, HEIGHT = 600, 400
FPS = 30

C_BG       = (15, 15, 25)
C_PANEL    = (30, 30, 50)
C_WHITE    = (240, 240, 255)
C_ACCENT   = (120, 200, 255)
C_MUTED    = (100, 100, 130)
C_GREEN    = (80, 200, 120)
C_RED      = (220, 80, 80)
C_YELLOW   = (255, 200, 60)


def draw_ui(screen, fonts, player):
    font_large, font_medium, font_small = fonts

    screen.fill(C_BG)

    panel_rect = pygame.Rect(40, 40, WIDTH - 80, 260)
    pygame.draw.rect(screen, C_PANEL, panel_rect, border_radius=16)
    pygame.draw.rect(screen, C_ACCENT, panel_rect, width=1, border_radius=16)

    title_surf = font_large.render("♪ Music Player", True, C_ACCENT)
    screen.blit(title_surf, title_surf.get_rect(centerx=WIDTH // 2, y=55))

    track_name = player.get_track_name()
    if len(track_name) > 30:
        track_name = track_name[:27] + "..."
    track_surf = font_medium.render(track_name, True, C_WHITE)
    screen.blit(track_surf, track_surf.get_rect(centerx=WIDTH // 2, y=120))

    if player.playlist:
        idx_text = f"{player.current_index + 1} / {len(player.playlist)}"
        idx_surf = font_small.render(idx_text, True, C_MUTED)
        screen.blit(idx_surf, idx_surf.get_rect(centerx=WIDTH // 2, y=150))

    status = player.get_status()
    if "Играет" in status:
        status_color = C_GREEN
    elif "Пауза" in status:
        status_color = C_YELLOW
    else:
        status_color = C_RED
    status_surf = font_medium.render(status, True, status_color)
    screen.blit(status_surf, status_surf.get_rect(centerx=WIDTH // 2, y=185))

    pos = player.get_position()
    pos_text = f"{int(pos // 60):02d}:{int(pos % 60):02d}"
    pos_surf = font_small.render(pos_text, True, C_MUTED)
    screen.blit(pos_surf, pos_surf.get_rect(centerx=WIDTH // 2, y=220))

    bar_x, bar_y, bar_w, bar_h = 80, 250, WIDTH - 160, 8
    pygame.draw.rect(screen, C_MUTED, (bar_x, bar_y, bar_w, bar_h), border_radius=4)
    if player.is_playing:
        fill_w = int((pos % 30) / 30 * bar_w)
        pygame.draw.rect(screen, C_ACCENT, (bar_x, bar_y, fill_w, bar_h), border_radius=4)

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

    start_x = (WIDTH - total_width) // 2
    for surf in rendered:
        screen.blit(surf, (start_x, hint_y))
        start_x += surf.get_width() + 20


def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player 🎵")

    clock = pygame.time.Clock()

    fonts = (
        pygame.font.SysFont("Arial", 28, bold=True),
        pygame.font.SysFont("Arial", 22),
        pygame.font.SysFont("Arial", 16),
    )

    player = MusicPlayer(music_folder="music")

    running = True
    while running:

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

        draw_ui(screen, fonts, player)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()