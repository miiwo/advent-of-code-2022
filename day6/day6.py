def part1():
    startIndex = 0
    endIndex = 0
    seenAlpha = [0] * 1000

    with open("./input", "r") as elf_file:
        transmission = elf_file.read()

        for char in transmission:
            print(char)
            if seenAlpha[ord(char)]:
                startIndex = endIndex
                seenAlpha = [0] * 1000

            endIndex += 1
            seenAlpha[ord(char)] = 1
            if endIndex - startIndex == 4:
                break

        return startIndex


def part2():
    pass

print(part1())