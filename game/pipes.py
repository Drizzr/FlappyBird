import pygame
import random

pygame.init()

class Pipes:

    def __init__(self):
        self.pipe_surface = pygame.image.load("sprites/pipe-green.png").convert_alpha()
        self.pipe_height = [200, 300, 400]
        self.pipe_List = []
    
    def create_pipe(self):
        randomp = random.choice(self.pipe_height)
        bottom = self.pipe_surface.get_rect(midtop = (350, randomp))
        top = self.pipe_surface.get_rect(midbottom = (350, randomp - 150))
        return  top, bottom
    
    def move_pipes(self):
        for pipe in self.pipe_List:
            pipe.centerx -= 3

    def draw_pipes(self, screen):
        self.move_pipes()
        for pipe in self.pipe_List:
            if pipe.bottom >= 512:  
                screen.blit(self.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)
