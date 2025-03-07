import os
import sys

from datetime import datetime
from time import sleep

from algos.algo_glouton import algoGlouton
from algos.algo_rs import algoRS

from config import load_config
from excel_io.excel import ExcelMedecin, ExcelSolution, Voeux

from heuristics.heuristique import evaluate, satisfaction
from models import Metadata

print("\n📂 Chargement des configurations depuis le fichier 'config.properties'...")
config = load_config()
print("✅ Configurations chargées avec succès !")

print("📂 Chargement des données des médecins depuis le fichier 'medecins.xlsx'...")
excel_medecin = ExcelMedecin(r"./medecins.xlsx")
medecin_data = excel_medecin.read_medecins()
print(f"✅ Données des médecins chargées avec succès ! ({len(medecin_data.medecins_garde)} médecins de garde)")

sleep(1)

print("📂 Chargement des fichiers de vœux pour les gardes et astreintes...")
if "input_garde" in config and "input_astreinte" in config:
    if os.path.exists(config["input_garde"]) and os.path.exists(config["input_astreinte"]):
        voeux = Voeux(config["input_garde"], config["input_astreinte"])
    else:
        print("❌ Les fichiers de vœux spécifiés dans le fichier de configuration n'existent pas.")
        sys.exit(-1)
else : 
    print("❌ Aucun fichier de vœux n'a été spécifié dans le fichier de configuration.")
    sys.exit(-1)
    
begin_index, end_index = voeux.adjust_time(config["begin"], config["end"])
print("✅ Fichiers de vœux chargés avec succès !")

sleep(1)

print(f"📂 Chargement de la solution initiale depuis le fichier '{config['input_garde']}'...")
excel_solution = ExcelSolution(config["input_garde"])
solution = excel_solution.read_solution()
solution = solution[begin_index:end_index+1]
print("✅ Solution initiale chargée avec succès !")

sleep(1)

# Création des métadonnées
if "blocked_shifts" in config and config["blocked_shifts"] == "1":
    print("\n⌛ Recherche des créneaux bloqués...")
    metadata = Metadata(
        medecin_data,
        voeux.data,
        excel_solution.compute_blocked_gardes(),
        excel_solution.compute_blocked_astreintes(),
        config["last_garde"]
    )

    sleep(1)

    # Affichage des gardes et astreintes bloquées
    print("\n🔒 Gardes bloquées :", metadata.blocked_gardes)
    print("🔒 Astreintes bloquées :", metadata.blocked_astreintes)
else:
    print("Créneaux bloqués désactivés.")
    metadata = Metadata(
        medecin_data,
        voeux.data,
        {},
        {},
        config["last_garde"]
    )

sleep(1)

# Évaluation de la solution initiale
print("\n🧩 Évaluation de la solution initiale...")

sleep(1)

# Application de l'algorithme glouton
print("\n🔄 Exécution de l'algorithme glouton pour créer une solution...")
solution = algoGlouton(solution, metadata)
print(f"✅ Solution créée par l'algorithme glouton.")
print(f"🔍 Satisfaction de la solution : {evaluate(solution, metadata):.3f}")

sleep(1)

# Application de l'algorithme
print("\n📊 Exécution de l'algorithme...")
solutions = []
for i in range(10):
    print(f"📝 Itération {i+1}/10 " + ("⬛" * (i+1)), end="\n" if i == 9 else "\r")
    sol = algoRS(solution, metadata)
    score = evaluate(sol, metadata)
    solutions.append((sol, score))

solution = max(solutions, key=lambda x: x[1])[0]
print("✅ Optimisation terminée.")
print(f"🔍 Satisfaction finale de la solution : {evaluate(solution, metadata):.3f}")

sleep(1)

# Génération d'un nom unique pour le fichier de sortie
output_filename = f"./output_solution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
print(f"\n💾 Enregistrement de la solution optimisée dans le fichier : {output_filename}...")
excel_solution.write_solution(solution, output_filename, begin_index)

print(f"📊 Génération du graphique de satisfaction...")
medecins = set(metadata.medecin_data.medecins_garde + metadata.medecin_data.medecins_astreinte)
excel_solution.write_graph({medecin: satisfaction(solution, metadata, medecin) for medecin in medecins}, output_filename)
print("✅ Solution enregistrée avec succès !")

print("\n🎉 Génération de planning terminée !")
