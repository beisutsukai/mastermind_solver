# Tester les fonctions :
print(get_pattern_max_numbers(4))

get_list_combinations(["RED", "ORANGE", "ROSE"], 1)
#[['RED', 'ORANGE', 'ROSE', 'RED'], ['RED', 'ORANGE', 'ROSE', 'ORANGE'], ['RED', 'ORANGE', 'ROSE', 'ROSE'], ['RED', 'ORANGE', 'ROSE', 'YELLOW'], ['RED', 'ORANGE', 'ROSE', 'GREEN'], ['RED', 'ORANGE', 'ROSE', 'BLUE'], ['RED', 'ORANGE', 'ROSE', 'VIOLET'], ['RED', 'ORANGE', 'ROSE', 'WHITE']]

combinaisons_totales = get_list_combinations([], 4)
print(len(combinaisons_totales))
# 4096

# La plus complexe, check_if_pattern_applies_on_combination() :
# On s'attend à vrai
check_if_pattern_applies_on_combination([0, 0, 4], ['RED', 'RED', 'RED', 'RED'], ['ORANGE', 'ORANGE', 'ORANGE', 'ORANGE'])

# On s'attend à faux : le 1er rouge ne peut pas être valide
check_if_pattern_applies_on_combination([0, 0, 4], ['RED', 'RED', 'RED', 'RED'], ['RED', 'ORANGE', 'ORANGE', 'ORANGE'])

# faux : aucune couleur commune
check_if_pattern_applies_on_combination([1, 0, 3], ['RED', 'RED', 'RED', 'RED'], ['BLUE', 'ORANGE', 'ORANGE', 'ORANGE'])

# vrai : couleur et position commune
check_if_pattern_applies_on_combination([1, 0, 3], ['RED', 'RED', 'RED', 'RED'], ['RED', 'ORANGE', 'ORANGE', 'ORANGE'])

# faux : couleur commune mais position différente
check_if_pattern_applies_on_combination([1, 0, 3], ['GREEN', 'RED', 'RED', 'RED'], ['RED', 'ORANGE', 'ORANGE', 'ORANGE'])

# vrai : 2 couleurs communes et position différente pour l'une
check_if_pattern_applies_on_combination([1, 1, 3], ['GREEN', 'RED', 'RED', 'RED'], ['RED', 'RED', 'ORANGE', 'ORANGE'])

# faux : la dernière couleur ne peut pas être la même (sinon on aurait un rouge de plus)
check_if_pattern_applies_on_combination([3, 0, 1], ['GREEN', 'RED', 'RED', 'RED'], ['GREEN', 'RED', 'RED', 'RED'])


# Calcul du nombre de combinaisons totales (avec 8 couleurs, 8 ^ nb de cases)
nb_cases = 4
nb_possibilities = pow(8, nb_cases)
print(nb_possibilities)
# 4096

# test de get_best_combination() pour seulement 3 cases (plus rapide)
list_all_combinations = get_list_combinations([], 3)
list_possible_combinations = get_list_combinations([], 3)
get_best_combination(list_all_combinations, list_possible_combinations, 3)
# tout est à 9 : pas si étonnant, contrairement à wordle, on n'a aucune combinaison plus fréquente que les autres
# rq : on pourrait mettre en dur n'importe quelle combinaison pour le 1er essai, pour accélérer les calculs


secret = ['GREEN', 'RED', 'RED', 'RED']
combination = ['GREEN', 'RED', 'RED', 'RED']
get_hints(combination, secret)
# [4, 0, 0]

combination = ['RED', 'GREEN', 'RED', 'BLUE']
get_hints(combination, secret)
# [1, 2, 1]

combination = ['YELLOW', 'GREEN', 'RED', 'BLUE']
get_hints(combination, secret)
# [1, 1, 2]



# Avec ce programme, on peut ainsi voir quel avantage donne le fait de n'avoir aucun résultat en testant juste deux couleurs
# par rapport au fait d'avoir 1 blanc

list_all_combinations = get_list_combinations([], 5)
len(list_all_combinations)
# 32768

# 1er exemple, on élimine deux couleurs dès le 1er essai
secret = ['GREEN', 'BLUE', 'RED', 'RED', "VIOLET"]
combination = ['WHITE', 'WHITE', 'YELLOW', 'YELLOW', 'YELLOW']
hints = get_hints(combination, secret)

combinaisons_possibles = get_combinations_compatible_with_hints(hints, combination, list_all_combinations)
len(combinaisons_possibles)
# 7776/32768 : 23.73% de combinaisons restantes

# 2e exemple, on a juste un indice blanc
combination = ['YELLOW', 'GREEN', 'YELLOW', 'YELLOW', 'GREEN']
hints = get_hints(combination, secret)
combinaisons_possibles = get_combinations_compatible_with_hints(hints, combination, list_all_combinations)
len(combinaisons_possibles)
