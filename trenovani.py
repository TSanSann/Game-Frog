import pygame


pygame.init()
# obrazovka
width = 700
height = 400

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Trenovani")
# definovani Barvy
rgb = 220,200,180
# urceni Bravy pozdani
screen.fill(rgb)
#hlavni cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
    pygame.display.update()


