def findPriority(item:chr):
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return ord(item) - 38

def findSharedItemInNGroup(group) -> int:
    didAppear = [0] * 52

    for index, member in enumerate(group[:-1]):
        for item in member:
            priority = findPriority(item)
            didAppear[priority - 1] = index + 1 if didAppear[priority - 1] == index else didAppear[priority - 1]

    for item in group[-1]:
        priority = findPriority(item)
        if didAppear[priority - 1] == len(group) - 1:
            return priority
    
    return 0



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
    group = []
    with open("./input", "r") as elf_file:
        for line in elf_file:
            if len(group) < 2:
                group.append(line)
            else:
                group.append(line)
                prioritySum += findSharedItemInNGroup(group)
                group = []
            
    return prioritySum
    

print(part1())
print(part2())