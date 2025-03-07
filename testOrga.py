from heuristics.verif import verifier_solution
from heuristics.heuristique import evaluate
from excel_io.excel import Voeux, ExcelSolution
from models import MedecinData
from algos.algo_genetique import algoOrga
from algos.algo_rs import algoRS
from algos.algo_tabou import algoTabou
from algos.algo_glouton import algoGlouton


from models import MedecinData, Metadata

voeux = Voeux(r"./input_garde_2.xlsx", r"./input_astreinte_1.xlsx")
excel_solution = ExcelSolution(r"./input_garde_2.xlsx")
solution = excel_solution.read_solution()

# print(planning.voeux)

medecins = list(voeux.data.keys())

specialisation = {"JMR", "MC", "PDS", "CP", "AVL", "FL", "JC", "SD", "GD", "MDT"}
Gmax = 100 ## todo : mettre une valeur cohÃ©rante
voeux_nbr_gardes = {medecin: 0 for medecin in medecins}

#print(medecins_de_garde, medecins_d_astreinte, specialisation, Gmax, voeux_nbr_gardes)

medecin_data = MedecinData(medecins, medecins, specialisation, Gmax, voeux_nbr_gardes)
metadata = Metadata(medecin_data, voeux.data, excel_solution.compute_blocked_gardes() ,excel_solution.compute_blocked_astreintes())

solution = algoGlouton(solution, metadata)


# ----------- INITIALISATION DU ORGA ----------------

population = []

population.append(solution)

#Sol1 (Solution fournie)
for i in range(10):
    if i%2 == 0:
        population.append(algoTabou(solution, metadata))
    population.append(algoRS(solution, metadata))

    

for i in population:
    print(f"pop init = {evaluate(i, metadata)}")


pop_finale = algoOrga(population, metadata, Pcross = 0.8, Pmut = 0.01, type_croisement="2point", masque=None, epochs = 10000)





    
print(verifier_solution(i, metadata))
print ("solution fin :", evaluate(pop_finale, metadata))