import sys, pygame
pygame.init()

box_x = 50
box_y = 50
box_width = 25
box_height = 25


size = width, height = 320,240
black = 0,0,0
white = 255,255,255
rect1 = pygame.Rect(50,50,25,25)

screen = pygame.display.set_mode(size)

while 1:
    
    screen.fill(black)
    pygame.draw.rect(screen, white, rect1)
    rect1 =  pygame.Rect(box_x,box_y,box_width,box_height)# pygame.Rect.move(rect1, (10,0))
    box_x += 0.01
    pygame.display.flip()
    