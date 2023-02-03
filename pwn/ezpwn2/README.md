# ez-pwn-2

## Point Value
75

## Challenge Description
Fun fact, I wrote this last friday because of a work related slack thread.
<br>Required reading:
<br>- intro to x86 https://www.cs.virginia.edu/~evans/cs216/guides/x86.html
<br>- x86-64 stack layout https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64
<br>- Stack Canaries https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/
<br>- stack based buffer overflows https://en.wikipedia.org/wiki/Stack_buffer_overflow 
<br>- ASLR https://en.wikipedia.org/wiki/Address_space_layout_randomization
<br>Optional Reading:
<br>- pwntools https://docs.pwntools.com/en/stable/intro.html#making-connections

<br><br><a href='/static/files/ez-pwn-2/ez-pwn-2'>ez-pwn-2</a>, <a href='/static/files/ez-pwn-2/ez-pwn-2.c'>source</a>

## Description
This is a simple pwnable that prints the current stack pointer and lets you state a pointer that you would like to read 8 bytes from in an infinite loop. It also has an unused function that literally just prints the flag. The read for the leaked pointer also has a buffer overflow vulnerability, so once players have leaked the return pointer to know where main is they should be able to calculate the the correct offset for the print flag function and return to it.

## Deployment
players need the ez-pwn-2 binary as well as ez-pwn-2.c, and the challenges needs a docker instance on the challenge server.