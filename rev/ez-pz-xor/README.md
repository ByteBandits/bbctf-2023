# Challenge points
125
# Challenge description
Whats the matter it's just an xor
# Included files
itsjustanxor

# Challenge solution
this challenge is a super simple xor with a global key but the binary has a c constructor that only sets the global xor key to the correct value if there is no debugger attached. there's also some extra code to make it hard to find a reference to this constructor.  When provided an input that xors correctly with the hidden key, the binary will read flag.txt from disk and print it out
