from pynput import keyboard
import time
import pygame
from songs import songs

pygame.init()

notes = {
    'A0': pygame.mixer.Sound('samples/A0.mp3'),
    'Bb0': pygame.mixer.Sound('samples/Bb0.mp3'),
    'A#0': pygame.mixer.Sound('samples/Bb0.mp3'),
    'B0': pygame.mixer.Sound('samples/B0.mp3'),
    'C1': pygame.mixer.Sound('samples/C1.mp3'),
    'Db1': pygame.mixer.Sound('samples/Db1.mp3'),
    'C#1': pygame.mixer.Sound('samples/Db1.mp3'),
    'D1': pygame.mixer.Sound('samples/D1.mp3'),
    'Eb1': pygame.mixer.Sound('samples/Eb1.mp3'),
    'D#1': pygame.mixer.Sound('samples/Eb1.mp3'),
    'E1': pygame.mixer.Sound('samples/E1.mp3'),
    'F1': pygame.mixer.Sound('samples/F1.mp3'),
    'Gb1': pygame.mixer.Sound('samples/Gb1.mp3'),
    'F#1': pygame.mixer.Sound('samples/Gb1.mp3'),
    'G1': pygame.mixer.Sound('samples/G1.mp3'),
    'Ab1': pygame.mixer.Sound('samples/Ab1.mp3'),
    'G#1': pygame.mixer.Sound('samples/Ab1.mp3'),
    'A1': pygame.mixer.Sound('samples/A1.mp3'),
    'Bb1': pygame.mixer.Sound('samples/Bb1.mp3'),
    'A#1': pygame.mixer.Sound('samples/Bb1.mp3'),
    'B1': pygame.mixer.Sound('samples/B1.mp3'),
    'C2': pygame.mixer.Sound('samples/C2.mp3'),
    'Db2': pygame.mixer.Sound('samples/Db2.mp3'),
    'C#2': pygame.mixer.Sound('samples/Db2.mp3'),
    'D2': pygame.mixer.Sound('samples/D2.mp3'),
    'Eb2': pygame.mixer.Sound('samples/Eb2.mp3'),
    'D#2': pygame.mixer.Sound('samples/Eb2.mp3'),
    'E2': pygame.mixer.Sound('samples/E2.mp3'),
    'F2': pygame.mixer.Sound('samples/F2.mp3'),
    'Gb2': pygame.mixer.Sound('samples/Gb2.mp3'),
    'F#2': pygame.mixer.Sound('samples/Gb2.mp3'),
    'G2': pygame.mixer.Sound('samples/G2.mp3'),
    'Ab2': pygame.mixer.Sound('samples/Ab2.mp3'),
    'G#2': pygame.mixer.Sound('samples/Ab2.mp3'),
    'A2': pygame.mixer.Sound('samples/A2.mp3'),
    'Bb2': pygame.mixer.Sound('samples/Bb2.mp3'),
    'A#2': pygame.mixer.Sound('samples/Bb2.mp3'),
    'B2': pygame.mixer.Sound('samples/B2.mp3'),
    'C3': pygame.mixer.Sound('samples/C3.mp3'),
    'Db3': pygame.mixer.Sound('samples/Db3.mp3'),
    'C#3': pygame.mixer.Sound('samples/Db3.mp3'),
    'D3': pygame.mixer.Sound('samples/D3.mp3'),
    'Eb3': pygame.mixer.Sound('samples/Eb3.mp3'),
    'D#3': pygame.mixer.Sound('samples/Eb3.mp3'),
    'E3': pygame.mixer.Sound('samples/E3.mp3'),
    'F3': pygame.mixer.Sound('samples/F3.mp3'),
    'Gb3': pygame.mixer.Sound('samples/Gb3.mp3'),
    'F#3': pygame.mixer.Sound('samples/Gb3.mp3'),
    'G3': pygame.mixer.Sound('samples/G3.mp3'),
    'Ab3': pygame.mixer.Sound('samples/Ab3.mp3'),
    'G#3': pygame.mixer.Sound('samples/Ab3.mp3'),
    'A3': pygame.mixer.Sound('samples/A3.mp3'),
    'Bb3': pygame.mixer.Sound('samples/Bb3.mp3'),
    'A#3': pygame.mixer.Sound('samples/Bb3.mp3'),
    'B3': pygame.mixer.Sound('samples/B3.mp3'),
    'C4': pygame.mixer.Sound('samples/C4.mp3'),
    'Db4': pygame.mixer.Sound('samples/Db4.mp3'),
    'C#4': pygame.mixer.Sound('samples/Db4.mp3'),
    'D4': pygame.mixer.Sound('samples/D4.mp3'),
    'Eb4': pygame.mixer.Sound('samples/Eb4.mp3'),
    'D#4': pygame.mixer.Sound('samples/Eb4.mp3'),
    'E4': pygame.mixer.Sound('samples/E4.mp3'),
    'F4': pygame.mixer.Sound('samples/F4.mp3'),
    'Gb4': pygame.mixer.Sound('samples/Gb4.mp3'),
    'F#4': pygame.mixer.Sound('samples/Gb4.mp3'),
    'G4': pygame.mixer.Sound('samples/G4.mp3'),
    'Ab4': pygame.mixer.Sound('samples/Ab4.mp3'),
    'G#4': pygame.mixer.Sound('samples/Ab4.mp3'),
    'A4': pygame.mixer.Sound('samples/A4.mp3'),
    'Bb4': pygame.mixer.Sound('samples/Bb4.mp3'),
    'A#4': pygame.mixer.Sound('samples/Bb4.mp3'),
    'B4': pygame.mixer.Sound('samples/B4.mp3'),
    'C5': pygame.mixer.Sound('samples/C5.mp3'),
    'Db5': pygame.mixer.Sound('samples/Db5.mp3'),
    'C#5': pygame.mixer.Sound('samples/Db5.mp3'),
    'D5': pygame.mixer.Sound('samples/D5.mp3'),
    'Eb5': pygame.mixer.Sound('samples/Eb5.mp3'),
    'D#5': pygame.mixer.Sound('samples/Eb5.mp3'),
    'E5': pygame.mixer.Sound('samples/E5.mp3'),
    'F5': pygame.mixer.Sound('samples/F5.mp3'),
    'Gb5': pygame.mixer.Sound('samples/Gb5.mp3'),
    'F#5': pygame.mixer.Sound('samples/Gb5.mp3'),
    'G5': pygame.mixer.Sound('samples/G5.mp3'),
    'Ab5': pygame.mixer.Sound('samples/Ab5.mp3'),
    'G#5': pygame.mixer.Sound('samples/Ab5.mp3'),
    'A5': pygame.mixer.Sound('samples/A5.mp3'),
    'Bb5': pygame.mixer.Sound('samples/Bb5.mp3'),
    'A#5': pygame.mixer.Sound('samples/Bb5.mp3'),
    'B5': pygame.mixer.Sound('samples/B5.mp3'),
    'C6': pygame.mixer.Sound('samples/C6.mp3'),
    'Db6': pygame.mixer.Sound('samples/Db6.mp3'),
    'C#6': pygame.mixer.Sound('samples/Db6.mp3'),
    'D6': pygame.mixer.Sound('samples/D6.mp3'),
    'Eb6': pygame.mixer.Sound('samples/Eb6.mp3'),
    'D#6': pygame.mixer.Sound('samples/Eb6.mp3'),
	'E6': pygame.mixer.Sound('samples/E6.mp3'),
    'F6': pygame.mixer.Sound('samples/F6.mp3'),
    'Gb6': pygame.mixer.Sound('samples/Gb6.mp3'),
    'F#6': pygame.mixer.Sound('samples/Gb6.mp3'),
    'G6': pygame.mixer.Sound('samples/G6.mp3'),
    'Ab6': pygame.mixer.Sound('samples/Ab6.mp3'),
    'G#6': pygame.mixer.Sound('samples/Ab6.mp3'),
    'A6': pygame.mixer.Sound('samples/A6.mp3'),
    'Bb6': pygame.mixer.Sound('samples/Bb6.mp3'),
    'A#6': pygame.mixer.Sound('samples/Bb6.mp3'),
    'B6': pygame.mixer.Sound('samples/B6.mp3'),
    'C7': pygame.mixer.Sound('samples/C7.mp3'),
    'Db7': pygame.mixer.Sound('samples/Db7.mp3'),
    'C#7': pygame.mixer.Sound('samples/Db7.mp3'),
    'D7': pygame.mixer.Sound('samples/D7.mp3'),
    'Eb7': pygame.mixer.Sound('samples/Eb7.mp3'),
    'D#7': pygame.mixer.Sound('samples/Eb7.mp3'),
    'E7': pygame.mixer.Sound('samples/E7.mp3'),
    'F7': pygame.mixer.Sound('samples/F7.mp3'),
    'Gb7': pygame.mixer.Sound('samples/Gb7.mp3'),
    'F#7': pygame.mixer.Sound('samples/Gb7.mp3'),
    'G7': pygame.mixer.Sound('samples/G7.mp3'),
    'Ab7': pygame.mixer.Sound('samples/Ab7.mp3'),
    'G#7': pygame.mixer.Sound('samples/Ab7.mp3'),
    'A7': pygame.mixer.Sound('samples/A7.mp3'),
    'Bb7': pygame.mixer.Sound('samples/Bb7.mp3'),
    'A#7': pygame.mixer.Sound('samples/Bb7.mp3'),
    'B7': pygame.mixer.Sound('samples/B7.mp3'),
    'C8': pygame.mixer.Sound('samples/C8.mp3'),
    ' ': pygame.mixer.Sound('samples/silence.mp3')
}

counter = 0

song = songs["L's theme"]

def on_press(key):
    global counter
    try:
        if counter >= 1:
            notes[song[counter-1]].stop()
                                
        notes[song[counter]].play() 
    except AttributeError:
        pass
    counter += 1
    if counter == len(song):
        counter = 0

# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
