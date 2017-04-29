import pygame
pygame.mixer.init()

pygame.mixer.music.load("/home/pi/Voice_reply/sad.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy(): 
    continue
