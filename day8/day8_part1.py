import sys

input_file_name = "day8_input_sample.txt" if "SAMPLE" in sys.argv else "day8_input.txt"


visible_trees = 0

with open(input_file_name) as input_file:
    trees_as_row = [list(line.strip()) for line in input_file.readlines()]
    trees_as_column = list(map(list, zip(*trees_as_row)))
    #print(trees_as_row)
    #print(trees_as_column)
    row_count = len(trees_as_row)
    column_count = len(trees_as_column)

    # Edges trees are visibles, of course
    visible_trees = ((row_count -1) + (column_count -1)) * 2

    # for other trees (ie not on edges)
    for x in range(1, row_count-1):
        for y in range(1, column_count-1):
            current_tree = int(trees_as_row[x][y])
            # identify trees around, on each direction
            trees_on_right  = trees_as_row[x][y+1:]
            trees_on_left   = trees_as_row[x][:y]
            trees_on_top    = trees_as_column[y][:x]
            trees_on_bottom = trees_as_column[y][x+1:]
            # identify highest tree, on each direction
            highest_tree_on_right  = max(trees_on_right)
            highest_tree_on_left   = max(trees_on_left)
            highest_tree_on_top    = max(trees_on_top)
            highest_tree_on_bottom = max(trees_on_bottom)
            print(f"{trees_on_right}->{highest_tree_on_right}, {trees_on_left}->{highest_tree_on_left}, {trees_on_top}->{highest_tree_on_top}, {trees_on_bottom}->{highest_tree_on_bottom}")

            if (any(int(tree_around) < current_tree for tree_around in [highest_tree_on_right, highest_tree_on_left, highest_tree_on_top, highest_tree_on_bottom])):
                # there is at least 1 tree, among the highest in the 4 directions, smaller than the current one
                visible_trees += 1

print(f"-------------------------------------------")
print(f"visible tree count: {visible_trees}")
