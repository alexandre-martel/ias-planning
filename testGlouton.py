from excel_io.excel import Voeux, ExcelSolution
from models import MedecinData, Metadata

from heuristics.heuristique import evaluate

from algos.algo_glouton import algoGlouton
from algos.algo_rs import algoRS

voeux = Voeux(r"./input_garde_2.xlsx", r"./input_astreinte_1.xlsx")

excel_solution = ExcelSolution(r"./input_garde_2.xlsx")
solution = excel_solution.read_solution()
    
medecins = set(voeux.data.keys())

print(medecins)

specialisation = {"JMR", "MC", "PDS", "CP", "AVL", "FL", "JC", "SD", "GD", "MDT"}

medecin_data = MedecinData(
    medecins_garde=medecins,
    medecins_astreinte=medecins,
    specialisation=specialisation,
    Gmax=3,
    voeux_nbr_gardes={medecin: 0 for medecin in medecins}
)

metadata = Metadata(medecin_data, voeux.data, excel_solution.compute_blocked_gardes(), excel_solution.compute_blocked_astreintes())

print(solution)
print(f"f(solution) = {evaluate(solution, metadata)}")

solution = algoGlouton(solution, metadata)

print(solution)
print(f"f(solution) = {evaluate(solution, metadata)}")

solution = algoRS(solution, metadata)

print(solution)
print(f"f(solution) = {evaluate(solution, metadata)}")
