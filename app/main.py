from game.game import Game
from game.bird import Bird
from game.floor import Floor
from game.pipes import Pipes
import pygame
import sys



pygame.init()


def gameLoop():
    floor = Floor()
    bird = Bird()
    pipes = Pipes()

    game = Game(bird, floor, pipes)

    while True:
        game.clock.tick(60)    
    
        if game.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.updateHighScore()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.Sound.play(game.wing_sound)
                        pygame.mixer.music.stop()
                        bird.bird_y_vel = 0
                        bird.bird_y_vel -= 6
                if event.type == game.SPAWNPIPE:
                    if len(pipes.pipe_List) > 3:
                        del pipes.pipe_List[0:2]
                    pipes.pipe_List.extend(pipes.create_pipe())
            
            # bg 
            game.screen.blit(game.bg_surf,(0, 0))
    
            #pipes
            pipes.draw_pipes(game.screen)
            
            game.score_display()
            
            # bird
            bird.bird_y_vel += game.GRAVITY
            bird.bird_rect.centery += bird.bird_y_vel
            bird.make_flap()
            bird.rotate_bird()
            game.screen.blit(bird.active_bird_surf, bird.bird_rect)
            game.check_collision()
            
            # floor
            floor.print_floor(game.screen)
            
            if game.check_point():
                game.score += 1

            # gameover screen
            if not game.run :
                pygame.mixer.Sound.play(game.die_sound)
                pygame.mixer.music.stop()
                for i in range(140):
                    game.screen.blit(game.gameover_screen, game.gameover_rect)
                    pygame.display.update()

            
                    
        else:
            if int(game.score) > int(game.high_score):
                game.high_score = game.score
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open("high_score.txt","w") as file:
                        file.write(str(int(game.score)))
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pipes.pipe_List.clear()
                        bird.bird_rect.center = (50, 256)
                        bird.bird_y_vel = 0
                        game.score = 0
                        game.run = True
            
            game.screen.blit(game.bg_surf,(0, 0))
            floor.print_floor(game.screen)
            game.screen.blit(game.start_screen, game.start_rec)
            game.score_display()
            
        pygame.display.update()


if __name__ == "__main__":
    gameLoop()
