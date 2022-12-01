import helper

# Part 1
print("Day 1 Part 1")
max_elf_inventory_total = 0
current_elf_iventory_total = 0

with open("./input", "r") as elf_file:
    for line in elf_file:
        if line in ["\n", "\r\n"]:
            max_elf_inventory_total = max(max_elf_inventory_total, current_elf_iventory_total)
            current_elf_iventory_total = 0
        else:
            current_elf_iventory_total += int(line)

print("---------------")
print(f"The total calories carried by the most /*gourmet*/ elf is: {max_elf_inventory_total} \n")

# Part 2
print("Day 1 Part 2")
current_elf_iventory_total = 0
top_three_elfs = helper.PriorityQueue()

with open("./input", "r") as elf_file:
    for line in elf_file:
        if line in ["\n", "\r\n"]:
            # store elf calories in a prio queue
            top_three_elfs.push(current_elf_iventory_total, current_elf_iventory_total)
            # trim so it only stores top 3 encountered
            if top_three_elfs.size() > 3:
                top_three_elfs.pop()
            current_elf_iventory_total = 0
        else:
            current_elf_iventory_total += int(line)

    # edge case: last elf's total calories does not have a new line after the file end, need to redo check
    top_three_elfs.push(current_elf_iventory_total, current_elf_iventory_total)
    if top_three_elfs.size() > 3:
        top_three_elfs.pop()

print("---------------")
elf_sum = top_three_elfs.pop() + top_three_elfs.pop() + top_three_elfs.pop()
print(f"The sum of the top 3 calorie favoring elves are: {elf_sum}")