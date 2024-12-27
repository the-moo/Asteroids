import pygame
from circleshape import CircleShape

class Asteroid (CircleShape):

    def __init__(self, x, y, radius):
        super().__init__ (x, y, radius)
        

    def draw(sceen, self):
        pygame.draw.circle (screen, white, self.position, self.radius, 2)

    def update(self):
        self.position = self.position + (self.velocity * dt)