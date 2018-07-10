#! /usr/bin/python
import sys
import os
import random
lives = 6
def check(num):
	global word
	global guess
	global show
	if len(word) > num:
		if word[num] == guess:
			show[num] = guess
with open('words.txt', 'r') as f:
	words = [line.strip() for line in f]
word = words[random.randint(0,999)]
'''
word = ""
print word
'''
show = []
wrongs = []
counter = 1
for counter in range(len(word)):
	show.append ("_")

##End game setup

print "Welcome to hangman, try to guess the word. You start with six lives. If you run out, you lose...\n"
gameon = 1
while gameon == 1:
	path = [('hang',), (str(lives),), ('.txt',)]
	path = "".join([x[0] for x in path])
	guy = open(path, 'r') 
	print guy.read()
	print show
	valid = 0
	while valid == 0:
		guess = raw_input ("Enter your letter: ")
		if len(guess) > 1:
			print "invalid"
		else:
			valid = 1
	if guess in word:
		print "Correct, the letter ",guess," is part of the word!"
		counter = 0
		for counter in range(len(word)):
			check(counter)
			counter += 1
		if "".join(str(x) for x in show) == word:
			print show
			sys.exit ("You win, Thanks for playing!")
	else:
		print "Incorrect, the letter ",guess," is not part of the word."
		wrongs.append(guess)
		print "Your wrong letters so far: ",wrongs
		lives -= 1
		if lives == 0:
			path = [('hang',), (str(lives),), ('.txt',)]
			path = "".join([x[0] for x in path])
			guy = open(path, 'r') 
			print guy.read()
			print "The word was ",word
			sys.exit ("You lose, Thanks for playing!")