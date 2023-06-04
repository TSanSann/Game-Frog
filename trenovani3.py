import pygame
import pygame.image
import random
# Odkaz ikony -    https://www.iconarchive.com/


pygame.init()
# obrazovka
width = 687
height = 457

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bažina-Jako-Svině")
# definovani Barvy
rgb = 220,200,180
white = 255,255,255
nadpis = 172, 45, 77, 0.938
rand_color = 144, 218,87
score_value = 0
fps = 350
# urceni Bravy pozdani
screen.fill(rgb)
# FONTY
#fonts = pygame.font.get_fonts()
#for certain_fot in fonts:
#   print(certain_fot)

s
# FPS a hodiny
clock = pygame.time.Clock()

# kristenitc

#nastaveni fotnu
system_font = pygame.font.SysFont("kristenitc", 30) # nastaveni fotu Bazina
system_font2 = pygame.font.SysFont("kristenitc", 20)


# font a text
system_text = system_font.render("Bažina", True, nadpis)
system_text_rect = system_text.get_rect()
system_text_rect.x = 300
system_text_rect.y = 15


# ZVUK 
# hudba v pozadi
pygame.mixer_music.load("./sounds/mode_song.wav")
# prehravani zvuku v pozadi
pygame.mixer_music.play(-1, 0)
# uprava Hlasitosti 1 = 100% , 0.3 = 30%
pygame.mixer_music.set_volume(0.3)


#zvuky
sound_frog = pygame.mixer.Sound("./sounds/frog_sound.wav")
sound_frog.set_volume(0.08)


# prehrani zvuku

# sound_frog.play()

#pygame.time.delay(2000)

# OBRAZEK
bacground_img = pygame.image.load("swamo.png")

harry_potter_image = pygame.image.load("frog.png")
hedvika_image = pygame.image.load("komarek.png")
bacground_rect = bacground_img.get_rect()
bacground_rect.topleft 
hedvika_rect = hedvika_image.get_rect()
hedvika_rect.x = 50
hedvika_rect.y = 100
harry_potter_rect = harry_potter_image.get_rect()
harry_potter_rect.center = (width//2,height//2)



#hlavni cyklus
lets_continue = True

while lets_continue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    lets_continue = False

              # zpomaleni cyklu - fps
            clock.tick(fps)
             # Implementovani skore
            score_text = system_font2.render(f"Score:{score_value}", True, white)
            score_text_rect = score_text.get_rect()
            score_text_rect.x = 15
            score_text_rect.y = 18

            screen.blit(bacground_img,bacground_rect)
            screen.blit(system_text, system_text_rect)
            screen.blit(harry_potter_image, harry_potter_rect)
            screen.blit(hedvika_image,hedvika_rect)
            screen.blit(score_text,score_text_rect)
           # kolize_ramecek_zabka = pygame.draw.rect(screen,white, harry_potter_rect,1,10)
          #  kolize_ramecek_komar = pygame.draw.rect(screen,white, hedvika_rect,1,10,100,400)
           


            zabka_movement = pygame.key.get_pressed()
            komar_movement = pygame.key.get_pressed()
        # Player 1 (zabka)
            if zabka_movement[pygame.K_s] and harry_potter_rect.bottom <= height:
                  harry_potter_rect.y = harry_potter_rect.y + 1
            if zabka_movement[pygame.K_w] and harry_potter_rect.top >= 0:
                   harry_potter_rect.y = harry_potter_rect.y - 1
            if zabka_movement[pygame.K_a] and harry_potter_rect.left >= 0:
                   harry_potter_rect.x = harry_potter_rect.x - 1
            if zabka_movement[pygame.K_d] and harry_potter_rect.right <= width:
                   harry_potter_rect.x = harry_potter_rect.x + 1
        # Player 2 (komar)         
            if komar_movement[pygame.K_DOWN] and hedvika_rect.bottom <= height:
                   hedvika_rect.y = hedvika_rect.y + 1
            if komar_movement[pygame.K_UP] and hedvika_rect.top >= 0:
                   hedvika_rect.y = hedvika_rect.y -1
            if komar_movement[pygame.K_LEFT] and hedvika_rect.left >= 0:
                   hedvika_rect.x = hedvika_rect.x -1
            if komar_movement[pygame.K_RIGHT] and hedvika_rect.right <= width:
                   hedvika_rect.x = hedvika_rect.x +1
       
            if harry_potter_rect.colliderect(hedvika_rect):
                   sound_frog.play()
                   score_value = score_value +1
                   hedvika_rect.x = random.randint(0 +45,width - 45)
                   hedvika_rect.y = random.randint(0 +32,height-32)

            pygame.display.update()



