from collections import deque

def part1() -> str:
    result = ""
    # make list of stacks
    supplyStacks = []

    with open("./input", "r") as elf_file:
        for line in elf_file:
            # for gods heaven, parse into a list of stacks
            # for somewhat bleh, parse the movement pattern
            sourceStack = 0
            targetStack = 0
            # move the items accordingly in stack
            supplyStacks[targetStack].append(supplyStacks[sourceStack].pop())
        # pop an element off each stack and return as result
    return result

def part2() -> int:
    result = 0
    with open("./input", "r") as elf_file:
        for line in elf_file:
            pass

    return result

print(part1())
print(part2())