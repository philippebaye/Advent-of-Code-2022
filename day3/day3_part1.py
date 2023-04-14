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
    for line in input_file:
        # compartement items repartitions
        rucksack = line.strip()
        items_count_in_rucksack = len(rucksack)
        items_count_in_each_compartment = items_count_in_rucksack // 2
        items_in_first_compartment = rucksack[:items_count_in_each_compartment]
        items_in_second_compartment = rucksack[items_count_in_each_compartment:]

        # intersect the 2 compartements, to find common items (normally only one)
        common_items = list(set(items_in_first_compartment) & set(items_in_second_compartment))
        priority = sum(priorities_by_items[item] for item in common_items)

        sum_of_priorities += priority


print(f"sum of all priorities = {sum_of_priorities}")
