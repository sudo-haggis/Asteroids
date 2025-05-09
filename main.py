import pygame
from constants import *
from player import * 

def main():
    print(f"Starting Asteroids!")
    pygame.init() 

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    #so this makes 2 groups, simple (dunow why its called sprite)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #create the screen with correct size from params
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #add the player class to the drawable and updatable group
    Player.containers = (drawable, updatable)

    #create new player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#000000")

        updatable.update(dt)

        #re-draw drawable things
        for drawthis in drawable:
            drawthis.draw(screen)

        #redraw  map, requested todo last (after player? weird?)        
        pygame.display.flip()

        #calc time taken to re-draw screen
        dt =  clock.tick(60) / 1000


if __name__ == "__main__":
    main()
