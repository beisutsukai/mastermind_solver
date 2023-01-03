import math
from itertools import combinations

COLORS = ["RED", "ORANGE", "ROSE", "YELLOW", "GREEN", "BLUE", "VIOLET", "WHITE"]

# Determines iterativally all the possible combinations given the chosen colors and boxes number
def get_list_combinations(combination, remaining_boxes):
    remaining_boxes = remaining_boxes - 1
    new_list_combinations = list()
    for color in COLORS:
        new_combination = combination.copy()
        new_combination.append(color)
        if remaining_boxes == 0:
            new_list_combinations.append(new_combination)
        if remaining_boxes > 0:
            new_list_combinations += get_list_combinations(new_combination, remaining_boxes)
    return new_list_combinations


def generate_patterns(nb_cases):
    patterns = list()
    for red_hints in range(0, nb_cases + 1):
        max_white_hints = nb_cases - red_hints
        for white_hints in range(0, max_white_hints + 1):
            no_hints = nb_cases - red_hints - white_hints
            pattern = [red_hints, white_hints, no_hints]
            patterns.append(pattern)
    return patterns

def check_if_pattern_applies_on_combination(pattern, pattern_combination, combination_to_validate):
    red_hints = pattern[0]
    white_hints = pattern[1]
    total_hints = red_hints + white_hints

    # If no hints at all, we just want to check that there are no common colors
    if total_hints == 0:
        for color_from_pattern in pattern_combination:
            if color_from_pattern in combination_to_validate:
                return False
        return True

    # Is there a common colors combination between pattern_combination and combination_to_validate ?
    color_possible_from_pattern  = list(combinations(pattern_combination, total_hints))
    color_possible_in_validation = list(combinations(combination_to_validate, total_hints))

    # convert to lists (can be sorted, but tuples cannot)
    color_possible_from_pattern = [list(ele) for ele in color_possible_from_pattern]
    color_possible_in_validation = [list(ele) for ele in color_possible_in_validation]
    [ele.sort() for ele in color_possible_from_pattern]
    [ele.sort() for ele in color_possible_in_validation]

    for color_combination in color_possible_from_pattern:
        color_combination = list(color_combination)
        color_combination.sort()  # sort to avoid some comparison problems (we are not checking the order yet, only colors)

        if color_combination in color_possible_in_validation:
            # We also have to check if the remaining colors (not in the common combination) are differents.
            # If not, false, because we should have more red or white hints
            remaining_pattern_colors = pattern_combination.copy()
            remaining_validation_colors = combination_to_validate.copy()
            for color in color_combination:
                remaining_pattern_colors.remove(color)
                remaining_validation_colors.remove(color)
            for remaining_color in remaining_pattern_colors:
                if remaining_color in remaining_validation_colors:
                    return False

            # Among colors in common, are there exactly as many at the same position as the red hints ?
            index_color = 0
            same_positions = 0
            for color_from_pattern in pattern_combination:
                if color_from_pattern in color_combination:
                    if pattern_combination[index_color] == combination_to_validate[index_color]:
                        same_positions = same_positions + 1
                        # We don't want to reuse a color that is only once in the common combination
                        color_combination.remove(color_from_pattern) # remove only remove first occurrence
                index_color = index_color + 1
            if same_positions == red_hints:
                return True
    return False


# For example with 4 boxes :
# There can be 0 to 4 reds, 0 to (4 - reds) whites, 0 to 4 - (reds + whites) empties
# So one pattern with 4 reds, two with three (1 white or 1 empty), three with 2 (two whites, one white, or zero), etc.
# PATTERN_NUMBERS =  1 + 2 + 3 + 4 + 5
def get_pattern_max_numbers(nb_boxes):
    result = 0
    for nb in range(1, nb_boxes + 2):  # +2 because range does not use the last element
        result = result + nb
    return result


def calculate_entropy(value):
    return - math.log(value) / math.log(2)


def get_best_combination(list_all_combinations, list_possible_combinations, nb_cases):
    nb_combinations_possibles_a_priori = len(list_possible_combinations)
    patterns    = generate_patterns(nb_cases)
    information_from_best_combination = 0
    best_combination = list()

    for guess_combination in list_all_combinations:
        list_entropy_by_pattern = list()
        for pattern in patterns:
            nb_combinations_ok = 0
            for combination_to_evaluate in list_possible_combinations:
                if check_if_pattern_applies_on_combination(pattern, guess_combination, combination_to_evaluate):
                    nb_combinations_ok = nb_combinations_ok + 1

            if nb_combinations_ok > 0: # If negative, no solutions, so the patterne cannot exist
                ratio = nb_combinations_ok / nb_combinations_possibles_a_priori
                information = calculate_entropy(ratio)
                list_entropy_by_pattern.append(information)

        mean_information = sum(list_entropy_by_pattern) / len(list_entropy_by_pattern)
        if mean_information > information_from_best_combination:
            best_combination = guess_combination
            information_from_best_combination = mean_information
            print("New best combination, information : " + str(mean_information) + " ; " + str(best_combination))

    print("Best combination : " + str(best_combination))
    return best_combination

def get_hints(_combination, _secret):
    secret = _secret.copy()
    combination = _combination.copy()
    nb_boxes = len(secret)
    red_hints = 0
    white_hints = 0
    # We first check the red hints, and then the whites, to avoid some particular situations
    # for example, if we think that a color corresponds to a white hint, but this color is twice in the combination,
    # and the second one is the only correct, corresponding to a red hint
    for color_index in range(0, len(combination)):
        if combination[color_index] == secret[color_index]:
            red_hints = red_hints + 1
            secret[color_index] = 'NULL_SECRET'
            combination[color_index] = 'NULL_COMB'
    # we now check white hints on a filtered list (without colors corresponding to red hints)
    for color in combination:
        if color in secret:
            white_hints = white_hints + 1
            index_secret = secret.index(color)
            index_comb = combination.index(color)
            secret[index_secret] = 'NULL_SECRET'
            combination[index_comb] = 'NULL_COMB'

    no_hints = nb_boxes - red_hints - white_hints
    return [red_hints, white_hints, no_hints]


def get_combinations_compatible_with_hints(pattern, guess_combination, list_possible_combinations):
    list_of_filtered_combinations = list()
    for combination_to_evaluate in list_possible_combinations:
        if check_if_pattern_applies_on_combination(pattern, guess_combination, combination_to_evaluate):
            list_of_filtered_combinations.append(combination_to_evaluate)
    return list_of_filtered_combinations


def is_secret_in_list(secret, list_combinations):
    if secret in list_combinations:
        return True
    return False

