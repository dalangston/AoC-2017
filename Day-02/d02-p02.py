#!/usr/bin/python3

import fileinput
import sys

numFile = "./input"

if (len(sys.argv) > 1):
	if (sys.argv[1] == "-f" and sys.argv[2] != ""):
		numFile = sys.argv[2]
	else:
		print("Usage:")
		print("\n" + sys.argv[0] + "[-f <filename>]")
		sys.exit(-1)

lineDiffs = []

for line in fileinput.input(numFile):
	lineList = line.split()
	#print(lineList)
	lineList = [int(i) for i in lineList]
	#print(lineList)
	
	lineList.sort(reverse=True)
	for i in range(len(lineList)):
		val = lineList[i]
		rlist = lineList[i+1:]

		if (len(rlist)):
			for curr in rlist:
				if (val % curr == 0):
					lineDiffs.append(val / curr)

print(sum(lineDiffs))
