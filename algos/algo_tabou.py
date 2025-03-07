from heuristics.verif import verifier_solution
from heuristics.heuristique import evaluate
import random

def get_neighbors(solution, metadata):
    neighbors = []
    for i in range(len(solution)):
           
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
                medecin = random.choice(list(metadata.medecin_data.medecins_garde))
                solution_modifiee[i] = (medecin, solution_modifiee[i][1])
            else:
                # Choisir un médecin d'astreinte aléatoire
                medecin = random.choice(list(metadata.medecin_data.medecins_astreinte))
                solution_modifiee[i] = (solution_modifiee[i][0], medecin)
        
        
            
            neighbors.append(solution_modifiee)
    return neighbors

def solution_to_hash(solution):
    return tuple(solution)

def aspiration_criterion(candidate_fitness, best_fitness):
    return candidate_fitness < best_fitness

def algoTabou(solution_initiale, metadata, max_iterations=100, tabou_size=10, debug=False):

    # Fonction d'évaluation
    f = lambda solution: evaluate(solution, metadata)

    # Initialisation
    solution_courante = solution_initiale
    best_solution = solution_initiale
    best_fitness = f(solution_initiale)
    
    tabu_list = []
    
    for iteration in range(max_iterations):
        voisins = get_neighbors(solution_courante, metadata)
        
        # Filtrer les voisins qui sont dans la liste tabou
        voisins_valables = [v for v in voisins if v not in tabu_list]
        
        # Si tous les voisins sont dans la liste tabou, les inclure de nouveau
        if not voisins_valables:
            voisins_valables = voisins
        
        # Évaluer les voisins et choisir le meilleur
        meilleur_voisin = max(voisins_valables, key=f)
        meilleur_fitness = f(meilleur_voisin)
        
        # Mettre à jour la meilleure solution globale
        if meilleur_fitness > best_fitness:
            best_solution = meilleur_voisin
            best_fitness = meilleur_fitness
        
        # Mettre à jour la solution courante et la liste tabou
        solution_courante = meilleur_voisin
        tabu_list.append(solution_courante)
        
        # Limiter la taille de la liste tabou
        if len(tabu_list) > tabou_size:
            tabu_list.pop(0)
        
        if debug:
            print(f"Itération {iteration+1} : Meilleure solution = {best_solution}, Score = {best_fitness}")

    return best_solution
