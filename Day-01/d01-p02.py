#!/usr/bin/python3

import sys
import fileinput

digitFile="./input.txt"

if (len(sys.argv) > 1 and sys.argv[1] == "-f"):
	digitFile=sys.argv[2]

for line in fileinput.input(digitFile):
	curr = 0
	last = len(line) - 2
	step = last / 2
	lineTotal = 0

	if (line[last] == line[0]):
		lineTotal += eval(line[0])

	while(curr < last):
		if (line[curr] == line[(curr + step) - last]):
			lineTotal += eval(line[curr])
		
		curr += 1

	print(lineTotal)

