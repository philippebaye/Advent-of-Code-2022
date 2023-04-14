import sys

input_file_name = "day4_input_sample.txt" if "SAMPLE" in sys.argv else "day4_input.txt"


#============================================================
# Extract first and last section of sections range assignment
#============================================================
def extract_edge_sections(sections_range: str) -> ():
    first_section, last_section = [int(edge_section) for edge_section in sections_range.split("-")]
    return first_section, last_section


fully_contained_assignments = 0

with open(input_file_name) as input_file:
    for line in input_file:
        # sections assigned for each elf
        elf1_sections_range_assignment, elf2_sections_range_assignment = line.strip().split(",")
        elf1_first_section, elf1_last_section = extract_edge_sections(elf1_sections_range_assignment)
        elf2_first_section, elf2_last_section = extract_edge_sections(elf2_sections_range_assignment)

        if (elf1_first_section <= elf2_first_section) and (elf1_last_section >= elf2_last_section):
            # elf 1 assigment fully contains elf 2 assigment
            fully_contained_assignments += 1
        elif (elf2_first_section <= elf1_first_section) and (elf2_last_section >= elf1_last_section):
            # elf 2 assigment fully contains elf 1 assigment
            fully_contained_assignments += 1

print(f"count of assigments fully contained by the other = {fully_contained_assignments}")
