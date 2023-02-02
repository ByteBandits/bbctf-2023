#!/usr/bin/env python3

BLOCKED = ["getattr", "eval", "exec", "breakpoint", "lambda", "help"]
BLOCKED = {func: None for func in BLOCKED}
BLOCKED['STATUS'] = 1

welcome='''
Please, stop this virus, he changed my environment


█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀ 
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄ 		but,

█▄█ █▀█ █░█   █▀▀ ▄▀█ █▄░█ ▀█▀   █▀▄ █▀▀ █▀▀ █▀▀ ▄▀█ ▀█▀   █▀▄▀█ █▀▀
░█░ █▄█ █▄█   █▄▄ █▀█ █░▀█ ░█░   █▄▀ ██▄ █▀░ ██▄ █▀█ ░█░   █░▀░█ ██▄

'''

print(welcome)

while True:
	BLOCKWORDS = ['builtins','setattr','getattr','system','import','read','S','subprocess','lower','dict','os','upper','1','8']
	if BLOCKED['STATUS']==0:
		flag=open('flag.txt','r')
		print(flag.read())
		break

	c = input('>>> ')
	BAD=""
	for i in BLOCKWORDS:
		if i in c:
			BAD=i
	
	if BAD!="":
		print("Sorry You cant write",BAD)

	else:
		try:
			print(eval(c,BLOCKED))
		except Exception as e:
			print("Useless Move, lol")