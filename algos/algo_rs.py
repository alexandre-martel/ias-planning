import random 
import math

from heuristics.heuristique import evaluate

def generer_voisin(solution, metadata):
    # Copier la solution pour ne pas modifier l'originale
    solution_modifiee = solution.copy()
    
    # Sélectionner deux créneaux aléatoires différents
    i, j = random.sample(range(len(solution)), 2)

    inverser = random.choice([True, False])
    garde = random.choice([True, False])

    if inverser:
        if garde:
            # Inverser les médecins de garde
            solution_modifiee[i] = (solution[j][0], solution_modifiee[i][1])
            solution_modifiee[j] = (solution[i][0], solution_modifiee[j][1])
        else:
            # Inverser les médecins d'astreinte
            solution_modifiee[i] = (solution_modifiee[i][0], solution[j][1])
            solution_modifiee[j] = (solution_modifiee[j][0], solution[i][1])
    else:
        if garde:
            # Choisir un médecin de garde aléatoire
            medecin = random.choice(metadata.medecin_data.medecins_garde) # l'input de random.choice doit étre une liste 
            solution_modifiee[i] = (medecin, solution_modifiee[i][1])
        else:
            # Choisir un médecin d'astreinte aléatoire
            medecin = random.choice(metadata.medecin_data.medecins_astreinte)
            solution_modifiee[i] = (solution_modifiee[i][0], medecin)
    
    return solution_modifiee


def algoRS(s_initial, metadata, f=evaluate, T_initial=100, alpha=0.9, T_min=1e-3, max_iter=1e7, nbiter_cycle=100):
    """
    Algorithme de recuit simulé pour maximiser une fonction f.
    
    :param f: Fonction à maximiser.
    :param T_initial: Température initiale.
    :param alpha: Facteur de refroidissement (0 < alpha < 1).
    :param T_min: Température minimale pour arrêter le processus.
    :param max_iter: Nombre maximal d'itérations.
    :param nbiter_cycle: Nombre d'itérations par cycle à température constante.
    :return: La meilleure solution trouvée.
    """

    s = s_initial
    best_solution = s
    best_score = f(s, metadata)
    T = T_initial
    k = 0
    
    while T > T_min and k < max_iter:
        # Démarrer un cycle de `nbiter_cycle` itérations à température constante
        for _ in range(nbiter_cycle):
            k += 1
            
            nouveau_voisin = generer_voisin(s, metadata)
            
            current_score = f(s, metadata)
            voisin_score = f(nouveau_voisin, metadata)
            
            # Calcul de la différence de score
            delta = voisin_score - current_score

            # Acceptation de la nouvelle solution selon les critères de recuit simulé
            if delta > 0 or random.random() < math.exp(delta / T):
                s = nouveau_voisin  # On accepte la solution voisine
                
                if voisin_score > best_score:
                    best_solution = nouveau_voisin
                    best_score = voisin_score

        # Refroidissement après chaque cycle
        T *= alpha
    
    return best_solution
