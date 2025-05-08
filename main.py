import pygame
from constants import *

def main():
    print(f"Starting Asteroids!")
    pygame.init() 

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#000000")
        pygame.display.flip()

        passed_time = clock.tick(60)
        dt = passed_time / 1000

if __name__ == "__main__":
    main()
