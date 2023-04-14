import sys
import string

input_file_name = "day3_input_sample.txt" if "SAMPLE" in sys.argv else "day3_input.txt"

#===========================
# Items and their priorities
#===========================
items = string.ascii_lowercase + string.ascii_uppercase
priorities = list(range(1, len(items)+1))
priorities_by_items = dict(zip(items, priorities))

sum_of_priorities = 0

with open(input_file_name) as input_file:
    all_rucksacks = [line.strip() for line in input_file]
    # group runcksacks by 3
    for i in range(0, len(all_rucksacks), 3):
        rucksack_1 = all_rucksacks[i]
        rucksack_2 = all_rucksacks[i+1]
        rucksack_3 = all_rucksacks[i+2]

        # instersect the 3 runcksacks, to find common items (normally only one)
        common_items = list(set(rucksack_1) & set(rucksack_2) & set(rucksack_3))
        priority = sum(priorities_by_items[item] for item in common_items)

        sum_of_priorities += priority


print(f"sum of all priorities = {sum_of_priorities}")
