import pygame


class Ball:
    
    RADIUS = 25
    STEP = 20
    COLOR = (220, 50, 50)
    OUTLINE_COLOR = (160, 20, 20)

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = screen_width // 2
        self.y = screen_height // 2

    def move(self, direction):
        new_x = self.x
        new_y = self.y

        if direction == 'up':
            new_y = self.y - self.STEP
        elif direction == 'down':
            new_y = self.y + self.STEP
        elif direction == 'left':
            new_x = self.x - self.STEP
        elif direction == 'right':
            new_x = self.x + self.STEP

        if self._in_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def _in_bounds(self, x, y):
        left_ok   = x - self.RADIUS >= 0
        right_ok  = x + self.RADIUS <= self.screen_width
        top_ok    = y - self.RADIUS >= 0
        bottom_ok = y + self.RADIUS <= self.screen_height
        return left_ok and right_ok and top_ok and bottom_ok

    def draw(self, screen):
        pygame.draw.circle(screen, self.OUTLINE_COLOR, (self.x, self.y), self.RADIUS + 2)
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.RADIUS)
        pygame.draw.circle(screen, (255, 180, 180), (self.x - 8, self.y - 8), 7)

    def get_position(self):
        return self.x, self.y