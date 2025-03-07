from excel_io.excel import Voeux, ExcelSolution
from models import MedecinData, Metadata

from heuristics.verif import verifier_solution
from heuristics.heuristique import evaluate
from algos.algo_rs import algoRS

voeux = Voeux(r"./input_garde_1.xlsx", r"./input_astreinte_1.xlsx")
excel_solution = ExcelSolution(r"./input_garde_1.xlsx")
solution = excel_solution.read_solution()

medecins_garde = {solution[i][0] for i in range(len(solution))}
medecins_astreinte = {solution[i][1] for i in range(len(solution))}

specialisation = {"JMR", "MC", "PDS", "CP", "AVL", "FL", "JC", "SD", "GD", "MDT"}
Gmax = 100 ## todo : mettre une valeur cohérante
voeux_nbr_gardes = {medecin: 0 for medecin in medecins_garde}

medecin_data = MedecinData(medecins_garde, medecins_astreinte, specialisation, Gmax, voeux_nbr_gardes)
metadata = Metadata(medecin_data, voeux.data, {}, {})

valid, message = verifier_solution(solution, metadata)
print(valid, message)

print(solution)
print(f"f(solution) = {evaluate(solution, metadata):.3f}")

solution = algoRS(solution, metadata)
print(solution)
print(f"f(solution) = {evaluate(solution, metadata):.3f}")
