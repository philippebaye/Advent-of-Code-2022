import sys
import re

#============================================================
# Configuration switch SAMPLE / NORMAL
#============================================================
if "SAMPLE" in sys.argv:
    input_file_name = "day5_input_sample.txt"
    arrangement = [''] * 3
else:
    input_file_name = "day5_input.txt"
    arrangement = [''] * 9

# pattern of step procedure input line
step_procedure_pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")

# flag : current input line concerns starting position of crates arrangement
is_starting_description_arrangement = True

with open(input_file_name) as input_file:
    for line in input_file:
        if not line.strip():
            # empty line -> starting arrangement description ending
            is_starting_description_arrangement = False
            continue

        if is_starting_description_arrangement:
            # Extract significant information from starting arrangement : crate name or stack number
            arrangement_row_length = len(line)
            row_arrangement = [line[i] for i in range(1, arrangement_row_length, 4)]

            if not row_arrangement[0] == "1":   # test if not footer line (i.e. not stacks numbers)
                for stack_index, crate_value in enumerate(row_arrangement):
                    if crate_value.strip():       # exploite only if have crave (ie not empty)
                        if not arrangement[stack_index]:
                            arrangement[stack_index] = []
                        arrangement[stack_index].append(crate_value)

        if not is_starting_description_arrangement:
            # Exploit step procedure
            #print(f"{arrangement = }")
            move_count, move_stack_from, move_stack_to = [int(i) for i in step_procedure_pattern.findall(line)[0]]
            #print(f"{move_count} {move_stack_from} {move_stack_to}")

            # crates moving
            for _ in range(0, move_count):
                crate_to_move = arrangement[move_stack_from-1].pop(0)
                #print(crate_to_move)
                arrangement[move_stack_to-1].insert(0, crate_to_move)

    print(f"final arrangement : \n{arrangement}")

    crates_on_top_of_each_stack = ''.join([crates[0] for crates in arrangement])
    print(f"crates on top: {crates_on_top_of_each_stack}")
