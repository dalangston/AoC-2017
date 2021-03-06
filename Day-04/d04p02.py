#!/usr/bin/python3

import sys, fileinput

pwList = "./input"

if (len(sys.argv) > 1):
	if (sys.argv[1] == "-f"):
		pwList = sys.argv[2]

valid = 0
invalid = 0

for phrase in fileinput.input(pwList):
	wordList = phrase.split()
	sortedWords = []

	for word in wordList:
		sortedWords.append(''.join(sorted(word)))

	if (len(sortedWords) == len(set(sortedWords))):
		valid += 1
	else:
		invalid += 1
		#print(str(wordList) + "\n" + str(set(wordList)))

print("Valid Passphrases:\t" + str(valid))
print("Invalid Passphrases:\t" + str(invalid))
