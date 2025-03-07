from heuristics.verif import verifier_solution
from itertools import product

def algoGlouton(s_initial, metadata):
    solution = s_initial.copy()

    medecins = set(metadata.voeux_data.keys())
    voeux_data = metadata.voeux_data
    blocked_gardes, blocked_astreintes = metadata.blocked_gardes, metadata.blocked_astreintes

    for i in range(len(solution)):
            gardes_sorted   = sorted(medecins, key=lambda x: (voeux_data[x][i][0], x), reverse=True)
            astreinte_sorted = sorted(medecins, key=lambda x: (voeux_data[x][i][1], x), reverse=True)

            for garde, astreinte in product(gardes_sorted, astreinte_sorted):

                if i in blocked_gardes and garde != blocked_gardes[i]:
                    continue

                if i in blocked_astreintes and astreinte != blocked_astreintes[i]:
                    continue
                
                solution[i] = (garde, astreinte)
                
                valid, _ = verifier_solution(solution[:i+1], metadata)

                if valid:
                    break
    
    if not verifier_solution(solution, metadata):
        print("L'algorithme glouton n'a pas réussi à générer une solution valide... (┬┬﹏┬┬)")

    return solution
