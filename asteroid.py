from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        #get velocity from parent
        self.move(dt)

    def move(self, dt) :
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle) * 1.2
        print(f"{angle} angle : {vector1}")
        vector2 = self.velocity.rotate(-angle)
        print(f"{-angle} angle : {vector2}")
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS 

        #create asteroid 1
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector1

        #create asteroid 2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector2
