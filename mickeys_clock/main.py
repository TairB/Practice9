import pygame
import time

pygame.init()

w, h = 600, 600
sc = pygame.display.set_mode((w, h))
pygame.display.set_caption("Mickey's Clock")

# Загружаем фон
bg = pygame.image.load("images/mickey_bg.png").convert_alpha()
bg = pygame.transform.scale(bg, (w, h))

# Загружаем руки
mh = pygame.image.load("images/right_hand.png").convert_alpha()  # минуты
sh = pygame.image.load("images/left_hand.png").convert_alpha()   # секунды

# Размер рук — подбери HAND_H если слишком длинные/короткие
HAND_W = 35
HAND_H = 200
mh = pygame.transform.scale(mh, (HAND_W, HAND_H))
sh = pygame.transform.scale(sh, (HAND_W, HAND_H))

font = pygame.font.SysFont("Arial", 36, bold=True)

def rab(image, angle, pos):
    ri = pygame.transform.rotate(image, angle)
    nr = ri.get_rect(center=pos)
    sc.blit(ri, nr.topleft)

clock_tick = pygame.time.Clock()
running = True

while running:
    sc.blit(bg, (0, 0))

    ct = time.localtime()
    m = ct.tm_min
    s = ct.tm_sec

    mg = -6 * m
    sg = -6 * s

    c = (w // 2, h // 2)
    rab(mh, mg, c)
    rab(sh, sg, c)

    pygame.draw.circle(sc, (30, 30, 30), c, 8)
    pygame.draw.circle(sc, (255, 255, 255), c, 4)

    text = font.render(f"{m:02d}:{s:02d}", True, (30, 30, 30))
    sc.blit(text, text.get_rect(center=(w // 2, h - 30)))

    pygame.display.flip()
    clock_tick.tick(30)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
