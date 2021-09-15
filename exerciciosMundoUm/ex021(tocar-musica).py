import pygame
from pygame.locals import *
from sys import exit
pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((225, 100))
pygame.display.set_caption('curta a música :)')
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
