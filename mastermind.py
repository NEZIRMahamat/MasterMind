import random

# Mastermind Game
#Propriètés statiques
LEN_RANDOM_LIST = 4
ROUND_GAME = 10
CHIFFRES = [1, 2, 3, 4, 5, 6]

# Génération combinaison sécrète aléatoire
def generate_random_numbers():
    secret_combinaison = random.sample(CHIFFRES, k=LEN_RANDOM_LIST)
    return secret_combinaison

# User input
def get_input_user_game():
    user_inputs = [int(x) for x in input(f"Indication ! Entrer 4 chiffres parmis {CHIFFRES} (séparés par des espaces, sans doublon) : ").split()]
    if len(set(user_inputs)) == LEN_RANDOM_LIST:
            # Vérifier les chiffres valides, qui sont la liste CHIFFRES
            if (min(user_inputs) in CHIFFRES and max(user_inputs) in CHIFFRES):
                return user_inputs
            else:
                print(f"Entrer 4 chiffres, parmis {CHIFFRES}, sans doublon: ")
                get_input_user_game()
    else:
        print(f'Exactement 4 chiffres réquis, parmis cet ensemble {CHIFFRES} sans doublon !')
        return get_input_user_game()


# Compare input user with combinaison solution
def compare_user_inputs_solution_game(combinaison_secrete, user_inputs):
    numbers_well_placed = []
    index_well_placed = 0
    numbers_loss_placed = []
    index_loss_placed = 0
    for index, item in enumerate(user_inputs):
        #chiffre correct à la bonne position
        if(combinaison_secrete[index]==item):
            index_well_placed +=1
            numbers_well_placed.append(f"{item}*")
        #chiffre correct à la mauvaise position
        elif(item in combinaison_secrete):
            numbers_loss_placed.append(f"{item}-")
            index_loss_placed +=1
    return numbers_well_placed, index_well_placed, numbers_loss_placed, index_loss_placed 

# Main principale du jeu
def main():
    secret_combinaison = generate_random_numbers()
    i_round = 1
    for i in range(1, ROUND_GAME+1):
        user_inputs = get_input_user_game()
        
        numbers_well_placed, index_well_placed, \
        numbers_loss_placed, index_loss_placed  = compare_user_inputs_solution_game(secret_combinaison, user_inputs)
        if(index_well_placed == LEN_RANDOM_LIST):
            print(f"Bravo, vous avez gagné -:) au bout de {i} tour(s)\
                    \nLa combinaison trouvée est : {secret_combinaison}") #break
            break
        # Afficher indices, chiffres bien placés
        elif(index_well_placed>0):
            print(f"Chiffres bien placés : {numbers_well_placed}")
        # Afficher les indices des chiffres mal placés
        elif(index_loss_placed>0):
            print(f"Chiffres mal placé : {numbers_loss_placed}")
    else:
        print(f"Vous avez perdu -:**:- au bout de {i} tours\
                \nLa combinaison attendue est : {secret_combinaison}")
        

if __name__=='__main__':
    main()
