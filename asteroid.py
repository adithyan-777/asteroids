import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        split_vecter1 = self.velocity.rotate(random_angle)
        split_vecter2 = self.velocity.rotate(-random_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        new_astroid1 = Asteroid(self.position.x, self.position.y, radius=split_radius)
        new_astroid2 = Asteroid(self.position.x, self.position.y, radius=split_radius)
        new_astroid1.velocity = split_vecter1 * 1.2
        new_astroid2.velocity = split_vecter2 * 1.2
