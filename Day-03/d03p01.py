#!/usr/bin/python3

import sys, fileinput, math

inputFile = "./input.txt"

if (len(sys.argv) > 1):
	if (sys.argv[1] == "-f"):
		inputFile = sys.argv[2]

def findRing(num):
	if (num == 1):
		return 1

	ring = 2
	while ((((2*ring)-1)**2) < num):
		ring += 1

	return ring

def findCorners(ring):
	sideLen = (2 * ring) - 1
	sideMax = sideLen ** 2

	c = [sideMax - (x * (sideLen - 1)) for x in range(4)]
	c.sort()
	return c
	#return [sideMax - (x * (sideLen - 1)) for x in range(4)]

def findSideCenter(num):
	ringNum = findRing(num)
	sideLen = (2 * ringNum) - 1
	corners = findCorners(ringNum)

	print("Ring:\t\t" + str(ringNum))
	print("Side:\t\t" + str(sideLen))
	print("Corners:\t" + str(corners))

	sideMax = 0

	for i in corners:
		if (num < i):
			sideMax = i
			break

	print("Chosen Corner:\t" + str(sideMax))
	return math.ceil(sideMax - sideLen / 2)

for number in fileinput.input(inputFile):
	memPos = int(number)
	steps = 0

	print("\n\nMem Pos:\t" + str(memPos))

	if (memPos > 1):
		myRing = findRing(memPos)
		sideCenter = findSideCenter(memPos)
		print("Side: Center:\t" + str(sideCenter))

		steps = ((myRing-1) + abs(memPos - sideCenter))# - 1
	print("Steps:\t\t" + str(steps))
