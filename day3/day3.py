def findPriority(item:chr):
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return ord(item) - 38

def findSharedItemInNGroup(*args) -> int:
    # item tracker of priority
    didAppear = [0] * 52

    for arg in args[:-1]:
        for item in arg:
            didAppear[findPriority(item) - 1] += 1

    for item in args[-1]:
        priority = findPriority(item)
        return priority if didAppear[priority - 1] == 2 else 0



def part1() -> int:
    # item tracker of priority
    didAppear = [0] * 52
    prioritySum = 0

    with open("./input", "r") as elf_file:
        for line in elf_file:
            firstCompartment = line[0:len(line)//2]
            secondCompartment = line[len(line)//2:]

            for item in firstCompartment:
                didAppear[findPriority(item) - 1] = 1

            for item in secondCompartment:
                priority = findPriority(item)
                if didAppear[priority - 1]:
                    prioritySum += priority
                    break
            
            # reset item tracker
            didAppear = [0] * 52

    return prioritySum

def part2() -> int:
    prioritySum = 0
    with open("./input", "r") as elf_file:
        for line in elf_file:
            pass
            # collect 3 lines at a time
            # run findSharedItemInNGroup
            # add to priority total
    return prioritySum
    

print(part1())
print(part2())