import pygame
from constants import *
from player import * 
from asteroid import *
from asteroidfield import *
from shot import *
import sys


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
    shots = pygame.sprite.Group()

    #create the screen with correct size from params
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #add the player class to the drawable and updatable group
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable #single things dont need no parenthesis
    asteroidField = AsteroidField()

    #create new player instance
    Player.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #create shot instaces
    Shot.containers = (drawable, updatable, shots)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#000000")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Collision detected")

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    #asteroid destroy
                    asteroid.split()
                    shot.kill()

        #re-draw drawable things
        for drawthis in drawable:
            drawthis.draw(screen)

        #redraw  map, requested todo last (after player? weird?)        
        pygame.display.flip()

        #calc time taken to re-draw screen
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
