# item tracker of priority
didAppear = [0] * 52
prioritySum = 0

def findPriority(item:chr):
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return ord(item) - 38

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

    print(prioritySum)

