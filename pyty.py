#!/usr/bin/python
#
# pyty -- a typewriter noise emulator built for Linux and X11
#
#   Copyright (C) 2012 Michael Holler <apotheos121 (at) gmail (dot) com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#
# Thanks to Tim Alexander <dragonfyre13@gmail.com> for his work in writing
# the pyxhook library packaged with the Simple Python Keylogger. It would
# have otherwise been a long and arduous process wrestling with the Xlib
# library without it.
#
# Thanks also to Theodore Watson and his NoisyTyper program for inspiring
# me to make my own, and thanks to Linux for not always having the solution
# available out of the box so that people like me can contribute.
#
# This software requires two non-standard packages:
# - python-xlib -- The Python interface for X, used to intercept keystrokes
# - mpg123      -- A command-line mp3 player, used to play the keyboard sounds
#
# On Ubuntu Linux, these packages can be installed by running the following
# line:
#       sudo apt-get install python-xlib mpg123
#

from random import choice
from pyxhook import HookManager
import signal, sys, time
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

def SigIntHandler(signum, frame):
    print ('Received SIGINT', file=sys.stderr)
    hm.cancel()
    time.sleep(0.2)
    sys.exit(0)

def main():
    signal.signal (signal.SIGINT, SigIntHandler)
    #hm.HookKeyboard()
    #hm.HookMouse()
    #hm.KeyDown = play_sound
    hm.KeyUp = play_sound
    hm.start()

if __name__ == '__main__':
    hm = HookManager()
    main()
    hm.join(1)
