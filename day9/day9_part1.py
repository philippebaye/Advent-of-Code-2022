'''
this script need python 3.10 or higher
'''

import sys

input_file_name = "day9_input_sample.txt" if "SAMPLE" in sys.argv else "day9_input.txt"


#===========================================
# Rope positions
#===========================================
STARTING_POSITION = (1,1)

# Current positions of the head and tail of the rope
head_current_position = STARTING_POSITION
tail_current_position = STARTING_POSITION

# All positions visited at least once by tail
all_tail_different_positions = {STARTING_POSITION}


#===========================================
# Move the tail, so that it fallows the head
#===========================================
def move_tail():
    global tail_current_position
    x_head, y_head = head_current_position
    x_tail, y_tail = tail_current_position

    # move tail according to gap between head and tail.
    match (x_head - x_tail, y_head - y_tail):
        case (0,0) | (1,0) | (-1,0) | (0,1) | (0,-1) | (1,1) | (1,-1) | (-1,1) | (-1,-1):
            ##print("no move")
            pass
        case (2,y):
            ##print("move")
            tail_current_position = (x_tail+1, y_head)
        case (-2,y):
            ##print("move")
            tail_current_position = (x_tail-1, y_head)
        case (x,2):
            ##print("move")
            tail_current_position = (x_head, y_tail+1)
        case (x,-2):
            ##print("move")
            tail_current_position = (x_head, y_tail-1)

    all_tail_different_positions.add(tail_current_position)


#==========================================
# Move the head of the rope as (x, y) shift
#==========================================
def move_head(x_moving:int, y_moving:int):
    global head_current_position
    x_head, y_head = head_current_position

    # moving on x coordinates axis
    x_step = 1 if x_moving > 0 else -1
    for x in range(0, x_moving, x_step):
        x_head += x_step
        head_current_position = (x_head, y_head)
        move_tail()

    # moving on y coordinates axis
    y_step = 1 if y_moving > 0 else -1
    for y in range(0, y_moving, y_step):
        y_head += y_step
        head_current_position = (x_head, y_head)
        move_tail()


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

        ##print(f"motion:{motion} -> head:{head_current_position}")


print(f"----------------------------------------")
##print(f"all tail different positions: {all_tail_different_positions}")
print(f"tail count differents positions: {len(all_tail_different_positions)}")
