import random
from heuristics.heuristique import evaluate


# ETAPE 0 : DEF Fonction

def choisir_sous_tableau(liste, valeurs_liste, N):
    newPop = []
    sum_fitness = sum(valeurs_liste)
    for _ in range(N):
        sum_ind, i = 0, 0
        ySF = random.random() * sum_fitness
        while sum_ind < ySF and i < len(valeurs_liste):
            sum_ind += valeurs_liste[i]
            i += 1
        newPop.append(liste[i - 1])  # Correction de l'index
    return newPop


def selection_par_tournoi(population, valeurs_liste, N, k=4):
    newPop = []
    for _ in range(N):
        # Sélectionner k individus au hasard
        candidats = random.sample(list(enumerate(population)), k)
        # Trouver l'individu avec la meilleure fitness parmi les candidats
        meilleur_individu = max(candidats, key=lambda x: valeurs_liste[x[0]])[1]
        newPop.append(meilleur_individu)
    return newPop


def algoOrga(population, metadata, Pcross = 0.8, Pmut = 0.01, type_croisement="2point", masque=None, epochs = 10000):
    

    for generation in range(epochs):
 
        valeurs_population = list(map(lambda s: evaluate(s, metadata), population))
        
        
        
        new_population = choisir_sous_tableau(population, valeurs_population, len(population))
        
        
        
        
       
        next_generation = []
        for _ in range(len(new_population) // 2):
            # Sélectionne deux parents par la méthode de la roulette
            
            individu1 = selection_par_tournoi(population, valeurs_population, 1)[0]
            individu2 = selection_par_tournoi(population, valeurs_population, 1)[0]
            
            # print("individu1 = " + str(individu1))
            # print("individu2 = " + str(individu2))

            
            if type_croisement == "1point":
                enfant1, enfant2 = croisement_1point(individu1, individu2, Pcross)
            elif type_croisement == "2point":
                enfant1, enfant2 = croisement_2point(individu1, individu2, Pcross)
            elif type_croisement == "masque" and masque:
                enfant1, enfant2 = croisement_masque(individu1, individu2, masque)
            else:
                enfant1, enfant2 = individu1, individu2  

            next_generation.extend([enfant1, enfant2])

        
        next_generation = [mutation(ind, Pmut, metadata) for ind in next_generation]

        
        population = next_generation

    
    valeurs_population = list(map(lambda s: evaluate(s, metadata), population))
    meilleur_individu = population[valeurs_population.index(max(valeurs_population))]

    return meilleur_individu
    

# ETAPE 4.1: On réalise les croisements. Pour l'instant, on choisit le croisement un point
def croisement_1point(individu1, individu2, Pcross):
    n = len(individu1)
    point_croisement = random.randint(1, n - 1)
    if random.random() < Pcross:
        # print("Croisement 1 point réalisé")
        enfant1 = individu1[:point_croisement] + individu2[point_croisement:]
        enfant2 = individu2[:point_croisement] + individu1[point_croisement:]
        # print("Enfant1" + str(enfant1))
        # print("Enfant2" + str(enfant2))
        return enfant1, enfant2
    else:
     
        return individu1, individu2


# ETAPE 4.2: Croisement deux points
def croisement_2point(individu1, individu2, Pcross):
    n = len(individu1)
    debut_croisement = random.randint(0, n - 1)
    fin_croisement = random.randint(debut_croisement, n - 1)
    
    if random.random() < Pcross:
        
        enfant1 = (individu1[:debut_croisement] + 
                   individu2[debut_croisement:fin_croisement + 1] + 
                   individu1[fin_croisement + 1:])
        
        enfant2 = (individu2[:debut_croisement] + 
                   individu1[debut_croisement:fin_croisement + 1] + 
                   individu2[fin_croisement + 1:])
        return enfant1, enfant2
    else:
        
        return individu1, individu2

# ETAPE 4.3: Croisement avec un masque
def croisement_masque(individu1, individu2, masque):
    ind1_croise, ind2_croise = [], []
    
    for i in range(len(masque)):
        if masque[i] == 1:
            ind1_croise.append(individu1[i])
            ind2_croise.append(individu2[i])
        else:
            ind1_croise.append(individu2[i])
            ind2_croise.append(individu1[i])
    
    return ind1_croise, ind2_croise
    
    
def mutation(individu, Pmut, metadata):
    n = len(individu)
    for i in range(n):
        # print("Epoch numero :", i)
        individu_modifiee = individu.copy()
        
        if random.random() < Pmut:
            # print("Pmut Validé")
            
            j = random.randint(0,len(individu)-1)
            
            inverser = random.choice([True, False])
            garde = random.choice([True, False])
            
            if inverser:
                if garde:
                    # Inverser les médecins de garde
                    individu_modifiee[i] = (individu[j][0], individu_modifiee[i][1])
                    individu_modifiee[j] = (individu[i][0], individu_modifiee[j][1])
                else:
                    # Inverser les médecins d'astreinte
                    individu_modifiee[i] = (individu_modifiee[i][0], individu[j][1])
                    individu_modifiee[j] = (individu_modifiee[j][0], individu[i][1])
            else:
                if garde:
                    # Choisir un médecin de garde aléatoire
                    medecin = random.choice(metadata.medecin_data.medecins_garde)
                    # print("choix", medecin)
                    individu_modifiee[i] = (medecin, individu_modifiee[i][1])
                else:
                    # Choisir un médecin d'astreinte aléatoire
                    medecin = random.choice(metadata.medecin_data.medecins_astreinte)
                    # print("choix", medecin)
                    individu_modifiee[i] = (individu_modifiee[i][0], medecin)
    return individu_modifiee


# def mutation(solution, Pmut, metadata):
#     # Copier la solution pour ne pas modifier l'originale
#     if random.random() < Pmut:
#         solution_modifiee = solution.copy()
        
#         # Sélectionner deux créneaux aléatoires différents
#         i, j = random.sample(range(len(solution)), 2)

#         inverser = random.choice([True, False])
#         garde = random.choice([True, False])

#         if inverser:
#             if garde:
#                 # Inverser les médecins de garde
#                 solution_modifiee[i] = (solution[j][0], solution_modifiee[i][1])
#                 solution_modifiee[j] = (solution[i][0], solution_modifiee[j][1])
#             else:
#                 # Inverser les médecins d'astreinte
#                 solution_modifiee[i] = (solution_modifiee[i][0], solution[j][1])
#                 solution_modifiee[j] = (solution_modifiee[j][0], solution[i][1])
#         else:
#             if garde:
#                 # Choisir un médecin de garde aléatoire
#                 medecin = random.choice(metadata.medecin_data.medecins_garde)
#                 solution_modifiee[i] = (medecin, solution_modifiee[i][1])
#             else:
#                 # Choisir un médecin d'astreinte aléatoire
#                 medecin = random.choice(metadata.medecin_data.medecins_astreinte)
#                 solution_modifiee[i] = (solution_modifiee[i][0], medecin)
        
#         return solution_modifiee
