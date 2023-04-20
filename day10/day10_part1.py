'''
this script need python 3.10 or higher
'''

import sys

input_file_name = "day10_input_sample.txt" if "SAMPLE" in sys.argv else "day10_input.txt"


# value of X register
register_x = 1
# cycle count
cycle = 1
# register already captured signal, to prevent register twice
signal_strengths_samples = set()
# list of signal strenghts at specific cycles
signal_strengths = []


#====================================
# Capture signal strength for a cycle
#====================================
def add_signal_strength_in_samples(cycle:int, register_value:int):
    if not cycle in signal_strengths_samples:
        signal_strengths_samples.add(cycle)
        signal_strengths.append(cycle  * register_value)
        print(f"register value at cycle: {cycle} -> {register_value}")


#=============================
# Process program instructions
#=============================
with open(input_file_name) as input_file:
    for instruction in input_file:

        match instruction.strip().split():
            case ["noop"]:
                print(f"instruction : noop")
                match cycle+1:
                    case 20|60|100|140|180|220:
                        # no more addx instruction possible before end of specific cycle
                        # => register current value of X register, for this specific cycle
                        print("noop cycle")
                        add_signal_strength_in_samples(cycle+1, register_x)
                cycle += 1

            case ["addx", value]:
                match cycle+1:
                    case 19|59|99|139|179|219:
                        # the instruction will end before the end of the specific cycle
                        # => value used in addx instruction, will be taken for this specific cycle
                        register_x += int(value)
                        add_signal_strength_in_samples(cycle+2, register_x)
                    case 20|60|100|140|180|220:
                        # specific cycle will end before the end of the instruction
                        # => register current value of X register, for this specific cycle
                        # => value used in addx instruction, will be taken for the next specific cycle
                        add_signal_strength_in_samples(cycle+1, register_x)
                        register_x += int(value)
                    case _:
                        register_x += int(value)
                cycle += 2
                print(f"instruction : {value} -> {register_x}")


print(f"----------------------------") 
print(f"signal strengths at specific cycles: {signal_strengths}")
print(f"sum of strengths: {sum(signal_strengths)}")
