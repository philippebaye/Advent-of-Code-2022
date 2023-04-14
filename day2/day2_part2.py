import sys

input_file_name = "day2_input_sample.txt" if "SAMPLE" in sys.argv else "day2_input.txt"

#===========================
# Values of each shape
#===========================
# Rock < Paper < Scissors < Rock
# 1    < 2     < 3        < 1
opponent_shapes_values = {'A': 1, 'B': 2, 'C': 3}

# Scores for the possible outcome of one round
POINTS_4_LOST_ROUND = 0
POINTS_4_DRAW_ROUND = 3
POINTS_4_WON_ROUND  = 6
outcomes_values = {'X': POINTS_4_LOST_ROUND, 'Y': POINTS_4_DRAW_ROUND, 'Z': POINTS_4_WON_ROUND}

# Total score of all rounds
total_score = 0

with open(input_file_name) as input_file:
    for line in input_file:
        # Convert choices as values
        opponent_choice, my_outcome_choice = line.strip().split()
        opponent_shape_value = opponent_shapes_values[opponent_choice]
        round_outcome = outcomes_values[my_outcome_choice]

        if round_outcome == POINTS_4_DRAW_ROUND:
            # same shape
            my_shape_value = opponent_shape_value
        elif round_outcome == POINTS_4_LOST_ROUND:
            if opponent_shape_value == 1:
                # Rock > Scissors
                my_shape_value = 3
            else: 
                # Paper > Rock or Scissors > Paper 
                my_shape_value = opponent_shape_value - 1
        else: # POINTS_4_WON_ROUND
            if opponent_shape_value == 3:
                # Scissors < Rock
                my_shape_value = 1
            else:
                # Rock < Paper or Paper < Scissors
                my_shape_value = opponent_shape_value + 1

        round_score = my_shape_value + round_outcome

        total_score += round_score

print(f"total score = {total_score}")
