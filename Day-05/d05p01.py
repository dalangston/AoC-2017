#!/usr/bin/python3

import sys, fileinput

inFile = "./input"

currInst = 0
nextInst = 0
lastInst = 0
jumpList = []
jumpCount = 0

for instruct in fileinput.input(inFile):
	jumpList.append(int(instruct))

lastInst = len(jumpList) - 1

while (currInst <= lastInst):
	nextInst = currInst + jumpList[currInst]
	jumpList[currInst] += 1
	jumpCount += 1
	currInst = nextInst

print("Exit:\t" + str(jumpCount) + " jumps")
