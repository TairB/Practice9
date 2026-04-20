import pygame
import datetime


class MickeyClock:
    
    def __init__(self, screen, center, hand_image_path):
       
        self.screen = screen
        self.center = center

        self.hand_original = pygame.image.load(hand_image_path).convert_alpha()

        self.hand_original = pygame.transform.scale(self.hand_original, (40, 120))

    def get_angle(self, value, max_value):
       
        return -(value / max_value) * 360

    def draw_hand(self, angle, color_offset=0):
      
        rotated = pygame.transform.rotate(self.hand_original, angle)

     
        rect = rotated.get_rect(center=self.center)

        self.screen.blit(rotated, rect)

    def draw(self):
      
        now = datetime.datetime.now()
        minutes = now.minute   # 0–59
        seconds = now.second   # 0–59

        minute_angle = self.get_angle(minutes, 60)
        second_angle = self.get_angle(seconds, 60)

      
        self.draw_hand(minute_angle)   
        self.draw_hand(second_angle)   

        return minutes, seconds
