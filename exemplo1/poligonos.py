import pygame

AMARELO = (255, 255, 0)
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)
RAIO = 50

pygame.init()

tela = pygame.display.set_mode((640, 480), 0)

while True:

    tela.fill(PRETO)

    pygame.draw.circle(tela, AMARELO, (60, 60), RAIO, 0)
    pygame.draw.rect(tela, VERDE, ((120, 15), (150, 100)), 0)

    pygame.display.update()


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()