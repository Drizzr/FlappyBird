import pygame

pygame.init()

class Floor:
    def __init__(self):
        self.floor_surf = pygame.image.load("sprites/base.png").convert_alpha()
        self.floor_position = 0

    def print_floor(self, screen):
        self.floor_position = 0 if self.floor_position < -288 else self.floor_position - 3
        screen.blit(self.floor_surf,(self.floor_position, 450))
        screen.blit(self.floor_surf,(self.floor_position + 288, 450))