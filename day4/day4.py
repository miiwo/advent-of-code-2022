def part1() -> int:
    result = 0
    with open("./input", "r") as elf_file:
        for line in elf_file:
            assignedSections = line.split(",")
            elfOne = assignedSections[0].split("-")
            elfTwo = assignedSections[1].split("-")

            if (int(elfOne[0]) <= int(elfTwo[0]) and int(elfOne[1]) >= int(elfTwo[1])) or (int(elfTwo[0]) <= int(elfOne[0]) and int(elfTwo[1]) >= int(elfOne[1])):
                result += 1

    return result

print(part1())
