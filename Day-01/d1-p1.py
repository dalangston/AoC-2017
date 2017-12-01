#!/usr/bin/python3

import fileinput


#digitFile="./input.txt"
#digitFile="./test-1.txt"
digitFile="./samples"

for line in fileinput.input(digitFile):
  print(line)
  lineTotal=0
  for digit in range(len(line)):
    if (digit < len(line)-1):
      if (line[digit] == line[digit+1]):
        print(str(digit) + ":  " + line[digit])
        lineTotal+=eval(line[digit])

  if (line[-1] == line[0]):
    print(str(digit) + ":  " + line[digit])
    lineTotal+=eval(line[digit])
      
  print(lineTotal)
