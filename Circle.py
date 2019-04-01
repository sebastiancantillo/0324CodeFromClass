import pygame

class Circle:
  def __init__(self, window, color, position, radius, speed):
    self.window = window
    self.color = color
    self.position = position
    self.radius = radius
    self.speed = speed

  def draw(self):
    pygame.draw.circle(self.window, self.color, self.position, self.radius)
    