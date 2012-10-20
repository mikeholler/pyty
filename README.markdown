pyty -- A Typewriter Noise Emulator for Linux
=============================================

pyty is the fullest-featured typewriter noise emulator available on the Linux
operating system. Bask in its glory! Admittedly it is a simple program, but
it needed to be done!

Why did I write a typewriter emulator for a computer? Because I was inspired by
Theodore Watson's OS X program, NoisyTyper, and by the fact that no suitable
alternative existed for Linux.

Installation
------------

**pyty was written on/for Ubuntu Linux, but it should work for any Unix-based
operating system**, provided it is running X and has the correct dependancies
installed.

What are the dependencies, you might ask? Here they are:
- **python-xlib** -- a Python library to interface with X
- **mpg123**      -- a command-line based mp3 player

On Ubuntu, these dependencies can be installed by running the following
command:

    sudo apt-get install python-xlib mpg123

### Starting pyty ###

Starting pyty couldn't be easier. Just open up a command prompt and type:

    python /path/to/pyty.py &

You're good to go!

### Stopping pyty ###

This will be fixed in the future (I just wanted to get this code up on GitHub
for people to see) but currently the only way to stop pyty without logging out
or rebooting is by finding its PID by running ``ps u`` and using ``kill`` with
the PID to end the process. Sorry for the inconvenience!


Closing Remarks
---------------

I certainly didn't write this without inspiration, and if my program inspires
you, all the better! **Feel free to fork, modify, and/or pull request.** Or, of
you're not that outgoing, at least open an issue if you'd like a feature added
or find something wrong with the program. I love collaborating with people, so
bring it on!

Enjoy!
