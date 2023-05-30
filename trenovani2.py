import pygame
# SPOUSTENI HRY /////////
pygame.init()
# ///////////////////////

# OBRAZOVKA ########################
width = 1000
height = 450

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Trenovani")
# definovani Barvy
rgb = 220,200,180
black = 0, 0, 0
yellow = 255, 255, 0
color = 200, 110, 88
blue = 0, 20, 220
# urceni Bravy pozdani
screen.fill(rgb)
# TVARY ((((((((((((((((((()))))))))))))))))))
# - čára
pygame.draw.line(screen, black, (0, 0), (width, height), 2)
# - kružnice
pygame.draw.circle(screen, yellow, (width//2, height//2), 100, 10)
# - kruh
pygame.draw.circle(screen, color, (width//2, height//2), 90, 0)
# - obdelnik (ctverec)
pygame.draw.rect(screen, blue, (width//2 - 50, height//2 - 50, 100, 100))
pygame.draw.line(screen, (255,255,255), (0,30), (50,30),2)


# ((((((((((((((((((((((((()))))))))))))))))))))))))
##################################################


#HLAVNI CYKLUS ***************************
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
    pygame.display.update()

# ****************************************