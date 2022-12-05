from collections import deque
import re

def part1() -> str:
    result = ""
    # make list of stacks
    supplyStacks = []
    doneInit = False

    with open("./input", "r") as elf_file:
        for line in elf_file:
            if line == "\n":
                doneInit = True
                continue
            if not doneInit:
                piles = re.findall("\D{3}\s|\n", line)
                for (index, pile) in enumerate(piles):
                    if len(supplyStacks) == 0:
                        supplyStacks = [deque() for x in range(len(piles))]
                    
                    if len(pile.strip()) != 0:
                        supplyStacks[index].appendleft(pile)
                continue
            # for somewhat bleh, parse the movement pattern
            moveCommands = re.findall("\d+", line)
            sourceStack = int(moveCommands[1]) - 1
            targetStack = int(moveCommands[2]) - 1
            # move the items accordingly in stack
            for i in range(0, min(int(moveCommands[0]), len(supplyStacks[sourceStack]))):
                supplyStacks[targetStack].append(supplyStacks[sourceStack].pop())
        # pop an element off each stack and return as result
    return list(map(lambda crate: crate.pop(), supplyStacks))

def part2() -> int:
    result = 0
    with open("./input", "r") as elf_file:
        for line in elf_file:
            pass

    return result

print(part1())
print(part2())