# Quiet
Plays a note per key typed on the keyboard

Hacked together very fast (most of the time was spent finding a suitable library of sound) so there's clearly lots of room for improvement.

Currently it loops L's theme and only if you type very slowly

## Usage: 
```
pip install -r requirements.txt
```
and run 
```python main.py```

in the *quiet* directory.

make a venv if you so please.

write your own songs and add them to songs.py as KV pairs.


### devnotes 
* keylogger to register keypresses
* dictionary of notes : notes (wav)
* play the wav when the key is pressed (long presses?)
* choosing a song
* discretizing a song into individual notes

