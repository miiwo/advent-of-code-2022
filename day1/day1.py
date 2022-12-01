import helper

# Part 1
print("Day 1 Part 1...")
max_elf_inventory_total = 0
current_elf_iventory_total = 0

with open("./input", "r") as elf_file:
    for line in elf_file:
        if line in ["\n", "\r\n"]:
            max_elf_inventory_total = max(max_elf_inventory_total, current_elf_iventory_total)
            current_elf_iventory_total = 0
        else:
            current_elf_iventory_total += int(line)

print(max_elf_inventory_total)

# Part 2
print("Day 1 Part 2...")
current_elf_iventory_total = 0
top_three_elfs = helper.PriorityQueue()

with open("./input", "r") as elf_file:
    for line in elf_file:
        if line in ["\n", "\r\n"]:
            top_three_elfs.push(current_elf_iventory_total, current_elf_iventory_total)
            if top_three_elfs.size() > 3:
                top_three_elfs.pop()
            print(current_elf_iventory_total)
            current_elf_iventory_total = 0
        else:
            current_elf_iventory_total += int(line)

    # edge case: last elf's total calories
    top_three_elfs.push(current_elf_iventory_total, current_elf_iventory_total)
    # trim the priority queue
    while top_three_elfs.size() > 3:
        top_three_elfs.pop()


#print("----------")
#print(top_three_elfs.pop())
#print(top_three_elfs.pop())
#print(top_three_elfs.pop())
print("----------")
elf_sum = top_three_elfs.pop() + top_three_elfs.pop() + top_three_elfs.pop()
print(elf_sum)