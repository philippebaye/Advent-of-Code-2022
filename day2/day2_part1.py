import sys

input_file_name = "day2_input_sample.txt" if "SAMPLE" in sys.argv else "day2_input.txt"

#===========================
# Values of each shape
#===========================
# Rock < Paper < Scissors < Rock
# 1    < 2     < 3        < 1
opponent_shapes_values = {'A': 1, 'B': 2, 'C': 3}
my_shapes_values = {'X': 1, 'Y': 2, 'Z': 3}

# Scores for the possible outcome of one round
POINTS_4_LOST_ROUND = 0
POINTS_4_DRAW_ROUND = 3
POINTS_4_WON_ROUND  = 6

# Total score of all rounds
total_score = 0


with open(input_file_name) as input_file:
    for line in input_file:
        # Convert choices as shape value
        opponent_choice, my_choice = line.strip().split()
        opponent_shape_value = opponent_shapes_values[opponent_choice]
        my_shape_value = my_shapes_values[my_choice]

        delta_values = opponent_shape_value - my_shape_value

        if delta_values == 2 or delta_values == -1:
            # Scissors < Rock => delta = 2
            # Rock < Paper, Paper < Scissors => delta = -1
            round_outcome = POINTS_4_WON_ROUND
        elif delta_values == 0:
            # same choice
            round_outcome = POINTS_4_DRAW_ROUND
        else:
            round_outcome = POINTS_4_LOST_ROUND

        round_score = my_shape_value + round_outcome

        total_score += round_score

print(f"total score = {total_score}")
