def part1() -> int:
    result = 0
    with open("./input", "r") as elf_file:
        for line in elf_file:
            assignedSections = line.split(",")
            elfOne = assignedSections[0].split("-")
            elfTwo = assignedSections[1].split("-")
            
            if (elfOne[0] <= elfTwo[0] and elfOne[1] >= elfTwo[1]) or (elfTwo[0] <= elfOne[0] and elfTwo[1] >= elfOne[1]):
                result += 1

    return result

print(part1())
