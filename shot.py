import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, radius=self.radius, color="white", center=self.position, width=2)

    def update(self, dt):
        self.position += self.velocity * dt