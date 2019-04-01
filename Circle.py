import pygame
import random

class Circle:
  def __init__(self, window, color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)), position = (random.randrange(0, 320),random.randrange(0, 240)), radius=random.randrange(1, 100), speed=[0,0]):
    #todo: boundaries. Properties to stay on the screen
    self.window = window
    self.color = color
    self.position = position
    self.radius = radius
    self.speed = speed

  def draw(self):
    pygame.draw.circle(self.window, self.color, self.position, self.radius)

  def move(self):
    self.position = (self.position[0]+self.speed[0], self.position[1]+self.speed[1])

    if (self.position[0] < 0):
      print("left")
    if (self.position[0] > self.windowSize[0]):
      print("right")
    if (self.position[1] < 0):
      print("top")
    if (self.position[1] > self.windowSize[1]):
      print("bottom")

# Dictionary Format: {"top": "sticky", "bottom": "scroll", "left": "bounce", "right": "gone"}
  def setBoundaries(self, boundaryDictionary, windowSize):
    self.boundaries = boundaryDictionary
    self.windowSize = windowSize

    