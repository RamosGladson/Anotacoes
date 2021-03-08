#programa abra e reproduz mp3

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('belle.mp3')
pygame.music.play()
pygame.event.wait()