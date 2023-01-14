# Complete game example (4 boxes)
# If you don't know the secret, skip the lines using gethints(), and enter the hints manually for each round
list_all_combinations = get_list_combinations([], 4)
secret = ['GREEN', 'BLUE', 'RED', "VIOLET"]

# 1st round
get_best_combination(list_all_combinations, list_all_combinations, 4)

# New best combination, information : 1.117140933282137 ; ['RED', 'RED', 'RED', 'RED']
# New best combination, information : 2.1348927830125146 ; ['RED', 'RED', 'RED', 'ORANGE']
# New best combination, information : 2.264315901602972 ; ['RED', 'RED', 'ORANGE', 'ORANGE']
# New best combination, information : 2.53800705171021 ; ['RED', 'RED', 'ORANGE', 'ROSE']
# New best combination, information : 2.622489716114238 ; ['RED', 'ORANGE', 'ROSE', 'YELLOW']
# Best combination : ['RED', 'ORANGE', 'ROSE', 'YELLOW']

# Here we can see what is the best opening. In future games, you can use this opening without redoing th calculations
# As we can see, the average information is very close whatever the first combination, but some are slightly better.
# Note that opening with only one color is the worst options, far behind all the others

# We try this combination and see what the hints are
combination = ['RED', 'ORANGE', 'ROSE', 'YELLOW']
hints = get_hints(combination, secret)
# then we can use the hints to reduce the number of possible combinations
possible_combinations_1 = get_combinations_compatible_with_hints(hints, combination, list_all_combinations)
len(possible_combinations_1)
# 976 remaining on the initial 4096 possibilities

# 2nd round
get_best_combination(list_all_combinations, possible_combinations_1, 4)
# New best combination, information : 0.7282521724927502 ; ['RED', 'RED', 'RED', 'RED']
# New best combination, information : 1.5090173755409684 ; ['RED', 'RED', 'RED', 'ORANGE']
# New best combination, information : 1.997203879108418 ; ['RED', 'RED', 'RED', 'GREEN']
# New best combination, information : 2.3197276622902696 ; ['RED', 'RED', 'ORANGE', 'GREEN']
# New best combination, information : 2.4923544894404612 ; ['RED', 'RED', 'GREEN', 'BLUE']
# New best combination, information : 2.565239551229749 ; ['RED', 'ROSE', 'GREEN', 'BLUE']
# New best combination, information : 2.675515239494455 ; ['RED', 'GREEN', 'GREEN', 'BLUE']
# New best combination, information : 2.708476901830461 ; ['ORANGE', 'RED', 'GREEN', 'BLUE']
# New best combination, information : 2.724383468338469 ; ['ORANGE', 'GREEN', 'GREEN', 'BLUE']
# New best combination, information : 2.745740088782639 ; ['ORANGE', 'GREEN', 'BLUE', 'VIOLET']
# Best combination : ['ORANGE', 'GREEN', 'BLUE', 'VIOLET']
# ['ORANGE', 'GREEN', 'BLUE', 'VIOLET']

combination = ['ORANGE', 'GREEN', 'BLUE', 'VIOLET']
hints = get_hints(combination, secret)
possible_combinations_2 = get_combinations_compatible_with_hints(hints, combination, possible_combinations_1)
len(possible_combinations_2)
# 71

# 3rd round
get_best_combination(list_all_combinations, possible_combinations_2, 4)

# New best combination, information : 0.2425179028311449 ; ['RED', 'RED', 'RED', 'RED']
# ...
# New best combination, information : 2.8016424020582464 ; ['ORANGE', 'BLUE', 'WHITE', 'BLUE']
# New best combination, information : 2.813664930307459 ; ['ORANGE', 'WHITE', 'ORANGE', 'VIOLET']
# New best combination, information : 2.821735972565476 ; ['ORANGE', 'WHITE', 'GREEN', 'GREEN']
# New best combination, information : 2.871134066305073 ; ['WHITE', 'GREEN', 'ORANGE', 'ORANGE']
# Best combination : ['WHITE', 'GREEN', 'ORANGE', 'ORANGE']
# ['WHITE', 'GREEN', 'ORANGE', 'ORANGE']

combination = ['WHITE', 'GREEN', 'ORANGE', 'ORANGE']
hints = get_hints(combination, secret)
possible_combinations_3 = get_combinations_compatible_with_hints(hints, combination, possible_combinations_2)
len(possible_combinations_3)
# 16

# 4th round
get_best_combination(list_all_combinations, possible_combinations_3, 4)

# As we can seen, the program try even combinations that can't be the solution,
# because sometimes trying them will bring the most information
# New best combination, information : 0.6780719051126377 ; ['RED', 'RED', 'RED', 'RED']
# ...
# New best combination, information : 2.912537158749661 ; ['GREEN', 'BLUE', 'ROSE', 'VIOLET']
# Best combination : ['GREEN', 'BLUE', 'ROSE', 'VIOLET']
# ['GREEN', 'BLUE', 'ROSE', 'VIOLET']

combination = ['GREEN', 'BLUE', 'ROSE', 'VIOLET']
hints = get_hints(combination, secret)
possible_combinations_4 = get_combinations_compatible_with_hints(hints, combination, possible_combinations_3)
len(possible_combinations_4)
# 2

print(possible_combinations_4)
# [['GREEN', 'BLUE', 'RED', 'VIOLET'], ['GREEN', 'BLUE', 'YELLOW', 'VIOLET']]
# We have only two possibilities left. We could try them one by one, the program won't help us anymore

# 5th round
get_best_combination(list_all_combinations, possible_combinations_4, 4)
# New best combination, information : 1.0 ; ['RED', 'RED', 'RED', 'RED']
# Best combination : ['RED', 'RED', 'RED', 'RED']
# As we can see here, with only two combinations left, it's not ideal to try every combination
# Trying ['RED', 'RED', 'RED', 'RED'] will tell us if there is RED in secret, but we don't want to waste
# a round for that. Better to try directly one of the remaining possibilities.

get_best_combination(possible_combinations_4, possible_combinations_4, 4)
# New best combination, information : 1.0 ; ['GREEN', 'BLUE', 'RED', 'VIOLET']
# Best combination : ['GREEN', 'BLUE', 'RED', 'VIOLET']
# ['GREEN', 'BLUE', 'RED', 'VIOLET']

# And we are done !
hints = get_hints(combination, secret)
# [4, 0, 0]