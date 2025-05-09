import pygame
from constants import *
from player import * 
from asteroid import *
from asteroidfield import *

def main():
    print(f"Starting Asteroids!")
    pygame.init() 

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    #create the screen with correct size from params
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #add the player class to the drawable and updatable group
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #create new player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    
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
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
