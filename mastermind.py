import pandas as pd 
import numpy as np
import random

# Mastermind Game
def mastermind():
    #Initialisation du jeu
    chiffres = [1, 2, 3, 4, 5, 6]
    #colors = ['red', 'orange', 'blue', 'yellow', 'sky', 'green', 'white']
    combinaison = random.sample(chiffres, k=4)
    #print({str(index): value for index, value in enumerate(combinaison)})
    # Interaction avec le joueur
    def combin_gamer(tour):
        #input('Entrer une combinaison de 4 chiffres : ')
        while tour<11:
            try:
                input_gamer = [int(x) for x in input('Indices : Entrer un chiffre suivi d\'un espace.\nA votre clavier : ').split()]
            except(ValueError) as e:
                print('Entrer des chiffres, les autres valeurs ne sont pas autorisées')
                combin_gamer(tour+1)
            else: 
                if(len(input_gamer)==4):
                    print(input_gamer)
                    #Indices
                    response = []
                    for index, item in enumerate(input_gamer):
                        #chiffre correct à la bonne position
                        if(combinaison[index]==item):
                            print(f"Indices, valeur : {item}*")
                            response.append(item)
                        #chiffre correct à la mauvaise position
                        elif(item in combinaison):
                            print(f"Indices, valeur : {item}-")
                        
                    if(len(response) == len(combinaison)):
                            print(f"Bravo, vous avez gagné 😎😎 au bout de {tour} tour(s) \nLa combinaison trouvée : {combinaison}")
                            break
                    elif(tour==10):
                        print(f"Vous avez perdu 🤯🤯 au bout de {tour} tours\nLa combinaison attendue est : {combinaison}")
                        break
                    else:
                        combin_gamer(tour+1)
                else:
                    print('Exactement 4 chiffres réquis')
                    combin_gamer(tour+1)

    combin_gamer(1)

if __name__=='__main__':
    mastermind()

"""
Gestion des tours :
Limiter le nombre de tentatives à 10.
Afficher un message de victoire si le joueur devine 
la combinaison avant la fin des tentatives.
Afficher un message de défaite si le joueur n’a pas 
trouvé après 10 tentatives, et révéler la combinaison secrète.



"""


