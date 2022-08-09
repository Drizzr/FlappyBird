import pygame

pygame.init()
pygame.mixer.init()

class Game:
    screen = pygame.display.set_mode((288, 512))
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1200)
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1200)
    def __init__(self, bird, floor, pipes):
        self.clock = pygame.time.Clock()
        self.run = False
        self.GRAVITY = 0.25  
        self.score = 0
        self.high_score = self.readHighScore()
        self.scoreplus = 0
        self.bg_surf = pygame.image.load("sprites/background-day.png").convert_alpha()
        self.start_screen = pygame.image.load("sprites/message.png").convert_alpha()
        self.start_rec = self.start_screen.get_rect(center = (144,256))
        self.gameover_screen = pygame.image.load("sprites/gameover.png").convert_alpha()
        self.gameover_rect = self.gameover_screen.get_rect(center = (144,256))
        self.game_font = pygame.font.Font('text.TTF', 20)
        self.wing_sound = pygame.mixer.Sound('audio/wing.wav')
        self.die_sound = pygame.mixer.Sound("audio/hit.wav")
        self.point_sound = pygame.mixer.Sound("audio/point.wav")
        self.Bird = bird
        self.Floor = floor
        self.Pipes = pipes

    
    def readHighScore(self):
        with open("high_score.txt", "r") as datei:
            return int(datei.read())

    def check_collision(self):
        for pipe in self.Pipes.pipe_List:
            if self.Bird.bird_rect.colliderect(pipe):
                self.run = False     
        if self.Bird.bird_rect.top <= 0 or self.Bird.bird_rect.bottom >= 450:
            self.run = False
        

    def score_display(self):
        if self.run:
            score_surface = self.game_font.render(str(int(self.score)), True, (255,255,255))
            score_rect = score_surface.get_rect(center=(144,50))
            self.screen.blit(score_surface, score_rect)
        else:
            highscore_surface = self.game_font.render(f"High Score: {str(self.high_score)}", True, (255,255,255))
            highscore_rect = highscore_surface.get_rect(center=(144,425))
            self.screen.blit(highscore_surface, highscore_rect)
            score_surface = self.game_font.render(f"recent score: {str(int(self.score))}", True, (255,255,255))
            score_rect = score_surface.get_rect(center=(144,50))
            self.screen.blit(score_surface, score_rect)


    def check_point(self):
        a = False
        for pipe in self.Pipes.pipe_List:
            if self.Bird.bird_rect.centerx == pipe.centerx:
                a = True
                pygame.mixer.Sound.play(self.point_sound)
                pygame.mixer.music.stop()
        return a
    
    def updateHighScore(self):
        if self.score > self.high_score:
            with open("high_score.txt","w") as file:
                    file.write(str(int(self.high_score)))
            
