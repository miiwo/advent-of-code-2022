def part1():
    seenAlpha = [0] * 1000
    startIndex = 0

    with open("./input", "r") as elf_file:
        transmission = elf_file.read()

        for index, char in enumerate(transmission):
            if seenAlpha[ord(char)]:
                startIndex = index
                seenAlpha = [0] * 1000

            seenAlpha[ord(char)] = 1
            if index - startIndex == 4:
                return index

# cabdeft

def part2():
    pass

print(part1())