import pygame
from pygame.mixer import Sound

import os

SOUND_LOCATION = "audio/"

SOUNDS = {}
SONGS = {}

def load():
    filenames = []
    for _,_, files in os.walk(SOUND_LOCATION):
        for f in files:
            if f[-4:] == ".ogg":
                SOUNDS[f[:-4]] = Sound(SOUND_LOCATION + "/" + f)
            elif f[-4:] == ".mp3":
                SONGS[f[:-4]] = SOUND_LOCATION + "/" + f

def play_sound(sound):
    if sound in SOUNDS:
        SOUNDS[sound].stop()
        SOUNDS[sound].play()

def play_song(song):
    if song in SONGS:
        pygame.mixer.music.load(SONGS[song])
        pygame.mixer.music.play()

def stop_sounds():
    for key in SOUNDS:
        stop_sound(key)

def stop_sound(sound):
    SOUNDS[sound].stop()

def stop_song():
    pygame.mixer.music.stop()
