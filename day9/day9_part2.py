'''
this script need python 3.10 or higher
'''

import sys

#============================================================
# Configuration switch SAMPLE / NORMAL
#============================================================
if "SAMPLE2" in sys.argv:
    input_file_name = "day9_input_sample2.txt" 
elif "SAMPLE" in sys.argv:
    input_file_name = "day9_input_sample.txt" 
else:
     input_file_name = "day9_input.txt"


#===========================================
# Rope positions
#===========================================
STARTING_POSITION = (0,0)
KNOTS_COUNT = 10
HEAD_INDEX = 0
TAIL_INDEX = KNOTS_COUNT - 1

# Position of all knots of the rope, first index (ie 0) for head, last (ie 9) for tail
knots_positions = [STARTING_POSITION] * KNOTS_COUNT
tail_current_position = STARTING_POSITION

# All positions visited at least once by tail
all_tail_different_positions = {STARTING_POSITION}


#===================================================================================
# Move the knot at specific index, so that it fallows the knot at the previous index
#===================================================================================
def move_one_knot(knot_index:int):
    x_head, y_head = knots_positions[knot_index-1]
    x_tail, y_tail = knots_positions[knot_index]

    # move knot according to gap between it and previous knot.
    ##print(f"knot_index: {knot_index}", x_head - x_tail, y_head - y_tail)
    match (x_head - x_tail, y_head - y_tail):
        case (delta_x, delta_y) if delta_x in [-1,0,1] and delta_y in [-1,0,1]:
            ##print("no move")
            pass
        case _:
            match (delta_x):
                case 2:
                    new_x_tail = x_tail + 1
                case -2:
                    new_x_tail = x_tail - 1
                case _:
                    new_x_tail = x_head
            match (delta_y):
                case 2:
                    new_y_tail = y_tail + 1
                case -2:
                    new_y_tail = y_tail - 1
                case _:
                    new_y_tail = y_head
            knots_positions[knot_index] = (new_x_tail, new_y_tail)

    ##print(f"knot position : {knot_index}->{knots_positions[knot_index]}")


#======================================
# Move other knots, one after the other
#======================================
def move_other_knots():
    for knot_index in range(1, KNOTS_COUNT):
        move_one_knot(knot_index)

    all_tail_different_positions.add(knots_positions[TAIL_INDEX])


#==========================================
# Move the head of the rope as (x, y) shift
#==========================================
def move_head(x_moving:int, y_moving:int):
    x_head, y_head = knots_positions[HEAD_INDEX]

    # moving on x coordinates axis
    x_step = 1 if x_moving > 0 else -1
    for x in range(0, x_moving, x_step):
        x_head += x_step
        knots_positions[HEAD_INDEX] = (x_head, y_head)
        move_other_knots()

    # moving on y coordinates axis
    y_step = 1 if y_moving > 0 else -1
    for y in range(0, y_moving, y_step):
        y_head += y_step
        knots_positions[HEAD_INDEX] = (x_head, y_head)
        move_other_knots()


#===========================
# Process motions input file
#===========================
with open(input_file_name) as input_file:
    for motion in input_file:
        match motion.strip().split():
            case ["R", step]:
                move_head(int(step), 0)
            case ["L", step]:
                move_head(int(step)*(-1), 0)
            case ["U", step]:
                move_head(0, int(step))
            case ["D", step]:
                move_head(0, int(step)*(-1))

        ##print(f"motion:{motion} -> head:{knots_positions[HEAD_INDEX]}")
        ##print(f"final knot positions: {knots_positions}")

print(f"----------------------------------------")
##print(f"all tail different positions: {sorted(all_tail_different_positions)}")
print(f"tail count differents positions: {len(all_tail_different_positions)}")
