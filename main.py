import pygame, random
import os
from tkinter import *
pygame.mixer.init()

def play_music():
  song = random.choice(os.listdir("./sounds"))
  sound = pygame.mixer.Sound("./sounds/"+song)
  sound.play()

root = Tk()
frame = Frame(root, width=100, height=100).pack()
button = Button(frame, text="Play", command=play_music).pack()
root.mainloop()