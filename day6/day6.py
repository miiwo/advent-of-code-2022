def part1():
    seenAlpha = [0] * 1000
    startIndex = 0

    with open("./input", "r") as elf_file:
        transmission = elf_file.read()

        for index, char in enumerate(transmission):
            if seenAlpha[ord(char)]:
                startIndex = index
                seenAlpha = [0] * 1000

            seenAlpha[ord(char)] = index
            if index - startIndex == 4:
                return index

# cabdeftf

def part2():
    seenAlpha = [-1] * 1000
    startIndex = 0

    with open("./input", "r") as elf_file:
        transmission = elf_file.read()
        #transmission = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

        for index, char in enumerate(transmission[:-14]):
            if not anyDuplicate(transmission[index: index + 14]):
                return index + 14

def anyDuplicate(x):
    seenAlpha = [0] * 1000
    for char in x:
        if seenAlpha[ord(char)]:
            return True
        seenAlpha[ord(char)] = 1
    
    return False

print(part1())
print(part2())