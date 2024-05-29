from pynput import keyboard
import pygame
from songs import songs

pygame.init()

notes = {
    'A0': pygame.mixer.Sound('samples/A0.wav'),
    'A#0': pygame.mixer.Sound('samples/A#0.wav'),
    'B0': pygame.mixer.Sound('samples/B0.wav'),
    'C1': pygame.mixer.Sound('samples/C1.wav'),
    'C#1': pygame.mixer.Sound('samples/C#1.wav'),
    'D1': pygame.mixer.Sound('samples/D1.wav'),
    'D#1': pygame.mixer.Sound('samples/D#1.wav'),
    'E1': pygame.mixer.Sound('samples/E1.wav'),
    'F1': pygame.mixer.Sound('samples/F1.wav'),
    'F#1': pygame.mixer.Sound('samples/F#1.wav'),
    'G1': pygame.mixer.Sound('samples/G1.wav'),
    'G#1': pygame.mixer.Sound('samples/G#1.wav'),
    'A1': pygame.mixer.Sound('samples/A1.wav'),
    'A#1': pygame.mixer.Sound('samples/A#1.wav'),
    'B1': pygame.mixer.Sound('samples/B1.wav'),
    'C2': pygame.mixer.Sound('samples/C2.wav'),
    'C#2': pygame.mixer.Sound('samples/C#2.wav'),
    'D2': pygame.mixer.Sound('samples/D2.wav'),
    'D#2': pygame.mixer.Sound('samples/D#2.wav'),
    'E2': pygame.mixer.Sound('samples/E2.wav'),
    'F2': pygame.mixer.Sound('samples/F2.wav'),
    'F#2': pygame.mixer.Sound('samples/F#2.wav'),
    'G2': pygame.mixer.Sound('samples/G2.wav'),
    'G#2': pygame.mixer.Sound('samples/G#2.wav'),
    'A2': pygame.mixer.Sound('samples/A2.wav'),
    'A#2': pygame.mixer.Sound('samples/A#2.wav'),
    'B2': pygame.mixer.Sound('samples/B2.wav'),
    'C3': pygame.mixer.Sound('samples/C3.wav'),
    'C#3': pygame.mixer.Sound('samples/C#3.wav'),
    'D3': pygame.mixer.Sound('samples/D3.wav'),
    'D#3': pygame.mixer.Sound('samples/D#3.wav'),
    'E3': pygame.mixer.Sound('samples/E3.wav'),
    'F3': pygame.mixer.Sound('samples/F3.wav'),
    'F#3': pygame.mixer.Sound('samples/F#3.wav'),
    'G3': pygame.mixer.Sound('samples/G3.wav'),
    'G#3': pygame.mixer.Sound('samples/G#3.wav'),
    'A3': pygame.mixer.Sound('samples/A3.wav'),
    'A#3': pygame.mixer.Sound('samples/A#3.wav'),
    'B3': pygame.mixer.Sound('samples/B3.wav'),
    'C4': pygame.mixer.Sound('samples/C4.wav'),
    'C#4': pygame.mixer.Sound('samples/C#4.wav'),
    'D4': pygame.mixer.Sound('samples/D4.wav'),
    'D#4': pygame.mixer.Sound('samples/D#4.wav'),
    'E4': pygame.mixer.Sound('samples/E4.wav'),
    'F4': pygame.mixer.Sound('samples/F4.wav'),
    'F#4': pygame.mixer.Sound('samples/F#4.wav'),
    'G4': pygame.mixer.Sound('samples/G4.wav'),
    'G#4': pygame.mixer.Sound('samples/G#4.wav'),
    'A4': pygame.mixer.Sound('samples/A4.wav'),
    'A#4': pygame.mixer.Sound('samples/A#4.wav'),
    'B4': pygame.mixer.Sound('samples/B4.wav'),
    'C5': pygame.mixer.Sound('samples/C5.wav'),
    'C#5': pygame.mixer.Sound('samples/C#5.wav'),
    'D5': pygame.mixer.Sound('samples/D5.wav'),
    'D#5': pygame.mixer.Sound('samples/D#5.wav'),
    'E5': pygame.mixer.Sound('samples/E5.wav'),
    'F5': pygame.mixer.Sound('samples/F5.wav'),
    'F#5': pygame.mixer.Sound('samples/F#5.wav'),
    'G5': pygame.mixer.Sound('samples/G5.wav'),
    'G#5': pygame.mixer.Sound('samples/G#5.wav'),
    'A5': pygame.mixer.Sound('samples/A5.wav'),
    'A#5': pygame.mixer.Sound('samples/A#5.wav'),
    'B5': pygame.mixer.Sound('samples/B5.wav'),
    'C6': pygame.mixer.Sound('samples/C6.wav'),
    'C#6': pygame.mixer.Sound('samples/C#6.wav'),
    'D6': pygame.mixer.Sound('samples/D6.wav'),
    'D#6': pygame.mixer.Sound('samples/D#6.wav'),
    'E6': pygame.mixer.Sound('samples/E6.wav'),
    'F6': pygame.mixer.Sound('samples/F6.wav'),
    'F#6': pygame.mixer.Sound('samples/F#6.wav'),
    'G6': pygame.mixer.Sound('samples/G6.wav'),
    'G#6': pygame.mixer.Sound('samples/G#6.wav'),
    'A6': pygame.mixer.Sound('samples/A6.wav'),
    'A#6': pygame.mixer.Sound('samples/A#6.wav'),
    'B6': pygame.mixer.Sound('samples/B6.wav'),
    'C7': pygame.mixer.Sound('samples/C7.wav'),
    'C#7': pygame.mixer.Sound('samples/C#7.wav'),
    'D7': pygame.mixer.Sound('samples/D7.wav'),
    'D#7': pygame.mixer.Sound('samples/D#7.wav'),
    'E7': pygame.mixer.Sound('samples/E7.wav'),
    'F7': pygame.mixer.Sound('samples/F7.wav'),
    'F#7': pygame.mixer.Sound('samples/F#7.wav'),
    'G7': pygame.mixer.Sound('samples/G7.wav'),
    'G#7': pygame.mixer.Sound('samples/G#7.wav'),
    'A7': pygame.mixer.Sound('samples/A7.wav'),
    'A#7': pygame.mixer.Sound('samples/A#7.wav'),
    'B7': pygame.mixer.Sound('samples/B7.wav'),
    'C8': pygame.mixer.Sound('samples/C8.wav')
}
	
counter = 0

song = songs["il vento d'oro"]

def play_note(note):
    if note in notes:
        notes[note].play()

def on_press(key):
	global counter
	try:
		notes[song[counter]].play() 
	except AttributeError:
		pass
	counter += 1

# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
