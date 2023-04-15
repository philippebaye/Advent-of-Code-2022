import sys

input_file_name = "day8_input_sample.txt" if "SAMPLE" in sys.argv else "day8_input.txt"


def count_visible_trees(current_tree:int, trees:[]) -> int:
    return next((index for index, tree in enumerate(trees) if int(tree) >= current_tree), len(trees)-1) +1


max_visible_trees_score = 0

with open(input_file_name) as input_file:
    trees_as_row = [list(line.strip()) for line in input_file.readlines()]
    trees_as_column = list(map(list, zip(*trees_as_row)))
    #print(trees_as_row)
    #print(trees_as_column)
    row_count = len(trees_as_row)
    column_count = len(trees_as_column)

    # for other trees (ie not on edges)
    for x in range(1, row_count-1):
        for y in range(1, column_count-1):
            current_tree = int(trees_as_row[x][y])
            # identify trees around, on each direction
            trees_on_right  = trees_as_row[x][y+1:]
            trees_on_left   = trees_as_row[x][:y]
            trees_on_top    = trees_as_column[y][:x]
            trees_on_bottom = trees_as_column[y][x+1:]
            # count visible trees, on each direction
            visible_trees_on_right = count_visible_trees(current_tree, trees_on_right)
            visible_trees_on_left = count_visible_trees(current_tree, trees_on_left[::-1])
            visible_trees_on_top = count_visible_trees(current_tree, trees_on_top[::-1])
            visible_trees_on_bottom = count_visible_trees(current_tree, trees_on_bottom)
            print(f"tree:{current_tree}, right:{trees_on_right}->{visible_trees_on_right}, left:{trees_on_left}->{visible_trees_on_left}, top:{trees_on_top}->{visible_trees_on_top}, bottom:{trees_on_bottom}->{visible_trees_on_bottom}")

            visible_trees_score = visible_trees_on_right * visible_trees_on_left * visible_trees_on_top * visible_trees_on_bottom

            if visible_trees_score > max_visible_trees_score:
                max_visible_trees_score = visible_trees_score

print(f"-------------------------------------------")
print(f"max visible tree score: {max_visible_trees_score}")
