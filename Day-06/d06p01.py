#!/usr/bin/python

import sys, fileinput

inFile = "./input"

def balance(mBanks):
    memBanks = mBanks
    lastIndex = len(memBanks) - 1
    maxVal = memBanks.index(max(memBanks))
    buffers = memBanks[maxVal]
    #print(memBanks)

    memBanks[maxVal] = 0
    currIndex = maxVal

    while (buffers):
        if (currIndex == lastIndex):
            currIndex = 0
        else:
            currIndex += 1

        memBanks[currIndex] += 1
        buffers -= 1

    #print(memBanks)

    return memBanks
        
banks = []
seenBanks = []

for line in fileinput.input(inFile):
    banks = [int(x) for x in line.split()]

seenBanks.append(banks)
balanceCount = 0

while (True):
    balanceCount += 1

    #print(balance(seenBanks[-1]))
    seenBanks.append(balance(seenBanks[-1]))
    print(seenBanks)

    if (seenBanks[-1] in seenBanks[:-1]):
        break


print("Infinite Loop Detected at:\t" + str(balanceCount) + " Steps.")

