import sys

input_file_name = "day1_input_sample.txt" if "SAMPLE" in sys.argv else "day1_input.txt"

# calories transported by current elf
calories = 0
# the max calories transported by one of elves
max_calories = 0

with open(input_file_name) as input_file:
    for line in input_file:
        if line.strip():
            calories += int(line)
        else:
            # break -> next elf
            if calories > max_calories: 
                max_calories = calories
            calories = 0

print(f"max calories = {max_calories}")
