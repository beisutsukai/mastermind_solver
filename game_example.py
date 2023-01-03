# Complete game example (4 boxes)
# If you don't know the secret, skip the lines using gethints(), and enter the hints manually for each round
list_all_combinations = get_list_combinations([], 4)
secret = ['GREEN', 'BLUE', 'RED', "VIOLET"]

# 1st round
get_best_combination(list_all_combinations, list_all_combinations, 4)

# New best combination, information : 5.068297655740561 ; ['RED', 'RED', 'RED', 'RED']
# New best combination, information : 5.593198437579674 ; ['RED', 'RED', 'RED', 'ORANGE']
# New best combination, information : 6.0743088151957405 ; ['RED', 'RED', 'ORANGE', 'ORANGE']
# Best combination : ['RED', 'RED', 'ORANGE', 'ORANGE']

# Here we can see what is the best opening. In future games, you can use this opening without redoing th calculations
# As we can see, the average information is very close whatever the first combination, but some are slightly better.
# Note that depending on if you play with 3, 4 or 5 boxes, the best opening won't be to use only two colors

# We try this combination and see what the hints are
combination = ['RED', 'RED', 'ORANGE', 'ORANGE']
hints = get_hints(combination, secret)
# then we can use the hints to reduce the number of possible combinations
possible_combinations_1 = get_combinations_compatible_with_hints(hints, combination, list_all_combinations)


# 2nd round
get_best_combination(list_all_combinations, possible_combinations_1, 4)

# New best combination, information : 1.0 ; ['RED', 'RED', 'RED', 'RED']
# New best combination, information : 1.207518749639422 ; ['RED', 'RED', 'RED', 'ORANGE']
# New best combination, information : 2.9343154345219467 ; ['RED', 'RED', 'RED', 'ROSE']
# New best combination, information : 3.882647428926194 ; ['RED', 'RED', 'ROSE', 'ROSE']
# New best combination, information : 4.199460121635386 ; ['RED', 'ORANGE', 'ROSE', 'ROSE']
# New best combination, information : 4.486866629320303 ; ['RED', 'ROSE', 'RED', 'ROSE']
# New best combination, information : 4.898551493218709 ; ['RED', 'ROSE', 'ROSE', 'ROSE']
# New best combination, information : 5.416116408019159 ; ['RED', 'ROSE', 'ROSE', 'YELLOW']
# New best combination, information : 5.425149502908122 ; ['ORANGE', 'ROSE', 'ROSE', 'YELLOW']
# Best combination : ['ORANGE', 'ROSE', 'ROSE', 'YELLOW']

combination = ['ORANGE', 'ROSE', 'ROSE', 'YELLOW']
hints = get_hints(combination, secret)
possible_combinations_2 = get_combinations_compatible_with_hints(hints, combination, possible_combinations_1)

# 3rd round
get_best_combination(list_all_combinations, possible_combinations_2, 4)

# New best combination, information : 1.0 ; ['RED', 'RED', 'RED', 'ORANGE']
# New best combination, information : 2.3776908414530706 ; ['RED', 'RED', 'RED', 'GREEN']
# New best combination, information : 2.7025890144346296 ; ['RED', 'RED', 'GREEN', 'GREEN']
# New best combination, information : 3.5559077853162457 ; ['RED', 'GREEN', 'RED', 'GREEN']
# New best combination, information : 3.9653209053757874 ; ['RED', 'GREEN', 'GREEN', 'BLUE']
# New best combination, information : 4.105563748774034 ; ['GREEN', 'GREEN', 'RED', 'GREEN']
# New best combination, information : 4.3612761490224825 ; ['GREEN', 'BLUE', 'RED', 'GREEN']
# New best combination, information : 4.450726794888022 ; ['GREEN', 'BLUE', 'RED', 'VIOLET']
# Best combination : ['GREEN', 'BLUE', 'RED', 'VIOLET']
# ['GREEN', 'BLUE', 'RED', 'VIOLET']

combination = ['GREEN', 'BLUE', 'RED', 'VIOLET']
hints = get_hints(combination, secret)
possible_combinations_3 = get_combinations_compatible_with_hints(hints, combination, possible_combinations_2)
print(possible_combinations_3)
# [['GREEN', 'BLUE', 'RED', 'VIOLET']]
# We are lucky here, we already found the secret combination (usually, it will require a couple more rounds)