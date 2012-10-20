from random import choice
from pyxhook import HookManager
import os

k_backspace = 'backspace.mp3'
k_return = 'return.mp3'
k_scrollDown = 'scrollDown.mp3'
k_scrollUp = 'scrollUp.mp3'
k_space = 'space.mp3'
k_generic = ['key-01.mp3',
             'key-02.mp3',
             'key-03.mp3',
             'key-04.mp3',
             'key-05.mp3']

def play_sound(event):
    if event.Key == 'Return':
        sound = k_return
    elif event.Key == 'Up':
        sound = k_scrollUp
    elif event.Key == 'Down':
        sound = k_scrollDown
    elif event.Key == 'space':
        sound = k_space
    elif event.Key == 'BackSpace':
        sound = k_backspace
    elif event.Ascii:
        sound = choice(k_generic)
    else:
        sound = None

    if sound:
        os.system('mpg123 --quiet sounds/{0} &'.format(sound))

def main():
    hm = HookManager()
    hm.HookKeyboard()
    hm.HookMouse()
    #hm.KeyDown = play_sound
    hm.KeyUp = play_sound
    hm.start()

if __name__ == '__main__':
    main()
