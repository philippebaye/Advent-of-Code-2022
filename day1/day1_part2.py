import sys

input_file_name = "day1_input_sample.txt" if "SAMPLE" in sys.argv else "day1_input.txt"

# calories transported by current elf
calories = 0
# calories transportes by all elves
all_calories = []

with open(input_file_name) as input_file:
    for line in input_file:
        if line.strip():
            calories += int(line)
        else:
            # break -> next elf
            all_calories.append(calories)
            calories = 0

# sort by DESC
all_calories.sort(reverse=True)
# sum the 3 first max calories
sum_of_top_3_calories = sum(all_calories[0:3])
print(f"sum of top 3 = {sum_of_top_3_calories}")
