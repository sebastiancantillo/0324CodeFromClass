import sys, pygame
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

ballRadius = 50
ball = pygame.draw.circle(screen, red, (0, 0), ballRadius)
ballSurface = pygame.Surface((ballRadius*2, ballRadius*2))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #ballrect = ballrect.move(speed)
    '''if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]'''

    screen.fill(backgroundColor)
    screen.blit(ballSurface, ball)
    pygame.display.flip()