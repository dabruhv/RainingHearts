import pygame
import random

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Valentine")
doexit = False


class hearts:
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        
        
    def draw(self):
        
        color1 = random.randrange(0,255)
        color2 = random.randrange(0,255)
        color3 = random.randrange(0,255)
        pygame.draw.circle(screen, (color1,color2,color3),(self.xpos,self.ypos),20)
        pygame.draw.circle(screen, (color1,color2,color3),(self.xpos+40,self.ypos),20)
        pygame.draw.polygon(screen,(color1,color2,color3),((self.xpos-20,self.ypos+5),(self.xpos+59, self.ypos+5),(self.xpos+20,self.ypos+50)))
        
    def move(self):
        if self.ypos > 800:
            self.ypos = 0
        self.ypos += random.randrange(1,10)
        
        
        
love = []
love =[hearts(random.randrange(0,800),random.randrange(0,800)) for i in range(90)]
        
        
while doexit == False:
    screen.fill((0,0,0))
    for hearts in love:
        hearts.draw()
        hearts.move()

    pygame.display.flip()
