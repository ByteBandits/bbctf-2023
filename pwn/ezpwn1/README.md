# ez-pwn-1

## Point Value
25

## Challenge Description
Memory safety? Whats that?
<br>Required Reading:
<br>- https://en.wikipedia.org/wiki/Stack_buffer_overflow
<br><br>
<a href='/static/files/ez-pwn-1/ez-pwn-1'>ez-pwn-1</a>, <a href='/static/files/ez-pwn-1/ez-pwn-1.c'>source</a>

## Description
dead simple pwnable, the stack contains an input buffer right above a string buffer that is passed to system(). by default the string buffer contains "ls" but it can be overflowed into with 8 bytes of padding followed by any arbitrary payload to system() to a max of 16 bytes. the flag is in a directory with a name thats 19 bytes long, so players need to be a little more creative than just running "cat flag.txt". The simplest solution is to just run /bin/sh
aaaaaaaa/bin/sh
cat the_flag_is_in_here/flag.txt

## Deployment
players should just get the ez-pwn-1.c and binary, and the challenges needs a docker instance on the challenge server.