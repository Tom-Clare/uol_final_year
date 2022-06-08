from pyo import *
from Sequencer_ext import Sequencer as Sequencer2
from SoundSequencer_ext import SoundSequencer
from BPM import BPM
from notes import notes
import pygame
from square import Square
import time
import threading

    
## Pygame code first

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREENWIDTH = 700
SCREENHEIGHT = 500

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("This is a test!")

#This will be a list of all game sprites
all_sprites_list = pygame.sprite.Group()

square = Square(WHITE,100,100)
square.rect.x = 0
square.rect.y = 0

# add square to list of sprites
all_sprites_list.add(square)


def GameLoop():
    
    #Main game code
    carryOn = True
    clock = pygame.time.Clock()
    i = 0

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        all_sprites_list.update()

        ## drawing logic
        screen.fill(BLACK)
        #pygame.draw.rect(screen, WHITE, [200, 300, 100, 100], 0)
        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

gameloop = threading.Thread(name="gameloop", target=GameLoop, daemon=True)
gameloop.start()

# plus_tot = [notes["D4"], notes["Fs4"], notes["A4"], notes["D4"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"]]


## Pyo code
########################################
## simple offbeat with hihat
s = Server().boot()

kicks = SoundSequencer(r"C:\Users\GLaDOS MkII\Documents\uni\projects\third_year\final_proj\project\sounds\kick.wav", [1,0,1,0,1,0,1,0], 0.4)
snares = SoundSequencer(r"C:\Users\GLaDOS MkII\Documents\uni\projects\third_year\final_proj\project\sounds\snare.wav", [0,0,1,0,0,0,1,0], 0.4)
ohats = SoundSequencer(r"C:\Users\GLaDOS MkII\Documents\uni\projects\third_year\final_proj\project\sounds\hat.wav", [1,1,1,1,1,1,1,1], 0.3)
bass = Sequencer2([0,notes['D2'],0,notes['D2'],0,notes['D2'],0,notes['D2']], mul=0.3)
bass_mix = bass.mix(2).out()



bpm = BPM(252, [kicks.next, snares.next, ohats.next, bass.next, square.newPos])

s.gui(locals())

