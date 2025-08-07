import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x ,y, radius):
        super().__init__(x ,y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, width=2, radius=self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(angle)
        vector_2 = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_1.velocity = vector_1 * 1.2
        new_asteroid_2.velocity = vector_2 * 1.2