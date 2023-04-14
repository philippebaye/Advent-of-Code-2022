import sys

input_file_name = "day4_input_sample.txt" if "SAMPLE" in sys.argv else "day4_input.txt"


#=================================================================
# Determine all sections included in the sections range assignment
#=================================================================
def define_all_sections(sections_range: str) -> []:
    first_section, last_section = [int(edge_section) for edge_section in sections_range.split("-")]
    #print(f"assignments {sections_range}: {first_section}, {last_section}")
    return [*range(first_section, last_section+1)]


overlap_assignments = 0

with open(input_file_name) as input_file:
    for line in input_file:
        # sections assigned for each elf
        elf1_sections_range_assignment, elf2_sections_range_assignment = line.strip().split(",")
        elf1_assigned_sections = define_all_sections(elf1_sections_range_assignment)
        elf2_assigned_sections = define_all_sections(elf2_sections_range_assignment)

        # check intersection between assigned sections
        if list(set(elf1_assigned_sections) & set(elf2_assigned_sections)):
            overlap_assignments += 1

print(f"overlaps count = {overlap_assignments}")
