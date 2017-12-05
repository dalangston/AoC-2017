## AoC 2017 - Day 05
Following and instruction jump list

### Part 1
Instructions are given as a list of jump offsets, positive or negative.  The program logic follows some rules:
- Jump <offset> steps to the next instruction.
- Increment the instruction you jumped from by 1
- How many jumps until you jump out of the "program"?

## Part 2
The program flow has changed.  If the offset is 3 or greater, decrement the offset by 1.  If it is less than 3, increment by 1.
