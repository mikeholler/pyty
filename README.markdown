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
operating system**, provided it is running X and has the correct dependencies
installed.

What are the dependencies, you might ask? Here they are:
- **python3-xlib** -- a Python library to interface with X
- **mpg123**      -- a command-line based mp3 player

On Ubuntu, these dependencies can be installed by running the following
command:

```sh
$ sudo apt-get install python3-xlib mpg123
```

### Starting pyty ###

Starting pyty couldn't be easier. Just open up a command prompt and type:

```sh
$ python3 /path/to/pyty.py &
```

Or simply:

```sh
$ /path/to/pyty.py &
```

To run this script on login, add the command to Startup Applications
(in Ubuntu) or the equivalent for your distribution.

You're good to go!

Closing Remarks
---------------

I certainly didn't write this without inspiration, and if my program inspires
you, all the better! **Feel free to fork, modify, and/or pull request.** Or, of
you're not that outgoing, at least open an issue if you'd like a feature added
or find something wrong with the program. I love collaborating with people, so
bring it on!

Enjoy!
