import pygame
import time


class MickeyClock:

    def __init__(self, screen, width, height):
        self.screen = screen
        self.w = width
        self.h = height
        self.center = (width // 2, height // 2)

        # Загружаем руки
        self.mh = pygame.image.load("images/right_hand.png").convert_alpha()
        self.sh = pygame.image.load("images/left_hand.png").convert_alpha()

        # Масштабируем
        self.mh = pygame.transform.scale(self.mh, (35, 170))
        self.sh = pygame.transform.scale(self.sh, (35, 170))

    def rab(self, image, angle, pos):
        """
        Вращает изображение и рисует с центром в pos.
        angle = -6 * value (360 / 60 = 6 градусов за единицу)
        минус = по часовой стрелке
        """
        ri = pygame.transform.rotate(image, angle)
        nr = ri.get_rect(center=pos)
        self.screen.blit(ri, nr.topleft)

    def draw(self):
        ct = time.localtime()
        m = ct.tm_min
        s = ct.tm_sec

        mg = -6 * m
        sg = -6 * s

        self.rab(self.mh, mg, self.center)
        self.rab(self.sh, sg, self.center)

        return m, s
