import pygame
from time import sleep

# Exercício: Abrindo e reproduzindo áudio MP3
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('lestGo.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)
