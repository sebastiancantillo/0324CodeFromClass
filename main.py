import sys, pygame
from Circle import *
pygame.init()

size = width, height = 320, 240
'''
Shorthand for:
width = 320
height = 240
size = (width, height)
'''

speed = [2, 2]
backgroundColor = (255, 255, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test")
ballPosition = (50,50)
ballRadius = 50

myCircle = Circle(screen, red, ballPosition, ballRadius, speed)
circleBlue = Circle(screen, (0,0,255))
circleCorner = Circle(screen, position=(320, 240))

defaultCircle = Circle(screen)
randomCircles = []
for i in range(10):
  randomCircles.append(Circle(screen))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(backgroundColor)
    #ballPosition = (ballPosition[0]+speed[0], ballPosition[1]+speed[1])

    #pygame.draw.circle(screen, red, ballPosition, ballRadius)

    myCircle.draw()
    defaultCircle.draw()
    for item in randomCircles:
      item.draw()
    circleBlue.draw()
    myCircle.move()
    circleCorner.draw()
    
    pygame.display.flip()