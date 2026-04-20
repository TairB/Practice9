import pygame
import datetime


class MickeyClock:
    """
    Класс часов Микки Мауса.
    Отображает текущее время (минуты и секунды) с помощью вращающихся рук.
    """

    def __init__(self, screen, center, hand_image_path):
        """
        screen          - поверхность Pygame для рисования
        center          - кортеж (x, y) — центр циферблата
        hand_image_path - путь к изображению руки Микки
        """
        self.screen = screen
        self.center = center

        # Загружаем изображение руки и сохраняем оригинал
        # convert_alpha() нужен для прозрачности (PNG с альфа-каналом)
        self.hand_original = pygame.image.load(hand_image_path).convert_alpha()

        # Масштабируем руку до нужного размера
        self.hand_original = pygame.transform.scale(self.hand_original, (40, 120))

    def get_angle(self, value, max_value):
        """
        Переводит текущее значение времени в угол поворота.
        
        Pygame rotate() вращает против часовой стрелки,
        поэтому берём отрицательный угол.
        
        Пример: 30 секунд из 60 = 180 градусов
        """
        return -(value / max_value) * 360

    def draw_hand(self, angle, color_offset=0):
        """
        Рисует одну руку под заданным углом.
        
        pygame.transform.rotate() вращает изображение вокруг его центра.
        После поворота нужно пересчитать позицию, чтобы рука была 
        привязана к центру циферблата.
        """
        # Поворачиваем оригинал (каждый раз оригинал, не повёрнутое изображение!)
        rotated = pygame.transform.rotate(self.hand_original, angle)

        # get_rect() с anchor в центре — чтобы рука вращалась вокруг нашей точки
        rect = rotated.get_rect(center=self.center)

        self.screen.blit(rotated, rect)

    def draw(self):
        """Рисует обе руки по текущему системному времени."""
        now = datetime.datetime.now()
        minutes = now.minute   # 0–59
        seconds = now.second   # 0–59

        # Рассчитываем углы
        minute_angle = self.get_angle(minutes, 60)
        second_angle = self.get_angle(seconds, 60)

        # Рисуем: сначала минутная рука (правая), потом секундная (левая)
        self.draw_hand(minute_angle)   # правая рука = минуты
        self.draw_hand(second_angle)   # левая рука = секунды

        return minutes, seconds
