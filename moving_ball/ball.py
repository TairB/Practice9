"""
Класс Ball — красный мяч, который движется по экрану.

Ключевые правила:
  1. Мяч НЕ может выйти за границы экрана
  2. Каждое нажатие = 20 пикселей
  3. Ввод игнорируется если мяч уже у края
"""

import pygame


class Ball:
    """
    Красный мяч 50×50 пикселей (радиус 25).
    """

    # Константы класса
    RADIUS = 25       # радиус = 25px
    STEP = 20         # шаг движения
    COLOR = (220, 50, 50)           # красный
    OUTLINE_COLOR = (160, 20, 20)   # тёмно-красный обводка

    def __init__(self, screen_width, screen_height):
        """Размещаем мяч в центре экрана."""
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Начальная позиция — центр экрана
        self.x = screen_width // 2
        self.y = screen_height // 2

    def move(self, direction):
        """
        Двигает мяч в указанном направлении.
        
        direction — одна из строк: 'up', 'down', 'left', 'right'
        
        Граничные условия:
          Минимальный x = RADIUS (чтобы мяч не вышел влево)
          Максимальный x = screen_width - RADIUS (чтобы не вышел вправо)
          Аналогично для y
        """
        new_x = self.x
        new_y = self.y

        # Вычисляем новую позицию
        if direction == 'up':
            new_y = self.y - self.STEP
        elif direction == 'down':
            new_y = self.y + self.STEP
        elif direction == 'left':
            new_x = self.x - self.STEP
        elif direction == 'right':
            new_x = self.x + self.STEP

        # Проверяем границы ПЕРЕД применением движения
        # Если новая позиция выходит за экран — игнорируем ввод
        if self._in_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y
        # Если не в границах — просто ничего не делаем (требование задания)

    def _in_bounds(self, x, y):
        """
        Возвращает True если позиция (x, y) находится внутри экрана.
        
        Мяч касается края когда: центр - радиус = 0 или центр + радиус = ширина
        """
        left_ok   = x - self.RADIUS >= 0
        right_ok  = x + self.RADIUS <= self.screen_width
        top_ok    = y - self.RADIUS >= 0
        bottom_ok = y + self.RADIUS <= self.screen_height
        return left_ok and right_ok and top_ok and bottom_ok

    def draw(self, screen):
        """
        Рисует мяч на экране.
        
        pygame.draw.circle(surface, color, center, radius, width)
          width=0 — залитый круг
          width>0 — только контур
        """
        # Внешний тёмный контур
        pygame.draw.circle(screen, self.OUTLINE_COLOR, (self.x, self.y), self.RADIUS + 2)
        # Основной красный круг
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.RADIUS)
        # Белый блик (декоративный)
        pygame.draw.circle(screen, (255, 180, 180), (self.x - 8, self.y - 8), 7)

    def get_position(self):
        """Возвращает текущую позицию мяча."""
        return self.x, self.y
