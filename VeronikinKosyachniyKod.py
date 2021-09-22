import pygame
from pygame.draw import *

screen = pygame.display.set_mode((1600, 800))

def main():
    fon()
    Ovalniy_man(130,250, True)
    Ovalniy_man(1270, 250, False)
    Triugolniy_man(600, True)
    Triugolniy_man(1000, False)
    heart()
    ice(800,280)
    ice(1450,430)
def fon():
    
    """Рисует фон. Аргументов не принимает, ни от чего не зависит. Хорошая функция."""
    
    rect(screen, '#afdafc', (0, 0, 1600, 400))
    rect(screen, '#30ba8f', (0, 400, 1600, 800))
def Ovalniy_man(x,y, side):
    
    """Рисует овального человека по заданным координатам. Если переменная side == False, отразит его по вертикали. """
    
    ellipse(screen, '#baacc7', (x, y, 140, 350))
    circle(screen, '#dcdcdc', (x + 70, y - 50), 70)
    if side == True:
        line(screen, 'black', (x + 30, y + 30), (x - 50, y + 200))
        line(screen, 'black', (x + 110, y + 30), (x + 270, y + 200))
    else:
        line(screen, 'black', (x + 110, y + 30), (x + 180, y + 200))
        line(screen, 'black', (x + 30, y + 30), (x - 70, y + 200))
    line(screen, 'black', (x + 30, 570), (x - 30, 730))
    line(screen, 'black', (x - 30, 730), (x - 30 - 30, 730))
    line(screen, 'black', (x + 110, 570), (x + 170, 730))
    line(screen, 'black', (x + 170, 730), (x + 200, 730))


    ellipse(screen, '#baacc7', (1270, 250, 140, 350))
    circle(screen, '#dcdcdc', (1340, 200), 70)
    
def Triugolniy_man(x,side):
    
    """Рисует треугольного человека по заданным координатам. Если переменная side == False, отразит его по вертикали. """
    
    k1 = 90 #подгоночный коэффициент 1
    k2 = 25 #подгоночный коэффициент 2
    
    if side == True:
        k3 = 10
        k4=200
        k5=110
    else:
        k3=-10
        k4=-200
        k5=-110
    polygon(screen, '#cf59b1', [(x, 230), (x-k1, 600), (x+k1, 600)])
    circle(screen, '#dcdcdc', (x, 200), 70)
    line(screen, 'black', (x-k3, 280), (x-k4, 450))
    line(screen, 'black', (x+k3, 280), (x+k5, 380))
    line(screen, 'black', (x+k5, 380), (x+k4, 280))
    line(screen, 'black', (x-k2, 600), (x-k2, 730))
    line(screen, 'black', (x-k2, 730), (x-k1, 730))
    line(screen, 'black', (x+k2, 600), (x+k2, 730))
    line(screen, 'black', (x+k2, 730), (x+k1, 730))

def heart():
    
     """Рисует сердце на верёвочке"""
    
    line(screen, 'black', (80, 460), (80, 200))
    polygon(screen, 'red', [(80, 250), (40, 150), (120, 145)])
    circle(screen, 'red', (60, 145), 25)
    circle(screen, 'red', (100, 145), 25)
   
    
def ice(x1,y1):
    
      """рисует мороженое. На верёвочке. Принимает на вход его координаты"""
    
    line(screen, 'black', (x1, y1), (x1, y1 - 100))
    polygon(screen, 'yellow', [(x1, y1 - 90), (x1 - 50, y1 - 190), (x1 + 50, y1 - 190)])
    circle(screen, 'red', (x1 + 25, y1 - 200), 25)
    circle(screen, 'brown', (x1 - 25, y1 - 200), 25)
    circle(screen, 'white', (x1, y1 - 240), 25)
   
    
main()

FPS = 30
clock = pygame.time.Clock()
finished = False

pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
