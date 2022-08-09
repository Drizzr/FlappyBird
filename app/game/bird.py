import pygame

pygame.init()

class Bird:
    def __init__(self):

        self.bird_y_vel = 0
        self.bird_movecount = 0 
        self.bird_surf_list = [pygame.image.load("static/sprites/bluebird-midflap.png").convert_alpha(), pygame.image.load("static/sprites/bluebird-downflap.png").convert_alpha(), pygame.image.load("static/sprites/bluebird-upflap.png").convert_alpha()]
        self.bird_rect = self.bird_surf_list[self.bird_movecount//5].get_rect(center = (100,512))
        self.active_bird_surf = None

    def make_flap(self):
        self.bird_movecount = 0 if self.bird_movecount >= 14 else self.bird_movecount + 1
        self.active_bird_surf = self.bird_surf_list[self.bird_movecount//5]
        
    
    def rotate_bird(self):
        self.active_bird_surf = pygame.transform.rotozoom(self.active_bird_surf, self.bird_y_vel * -1.2, 1)