from excel import Voeux, ExcelSolution

def datetime_to_string(datetime):
    return datetime.strftime("%Y-%m-%d")

print("📂 Chargement des fichiers de voeux...")
voeux = Voeux(r"./input_garde_2.xlsx", r"./input_astreinte_1.xlsx")
print("✅ Voeux chargés avec succès :")

# Lire la solution existante depuis le fichier Excel
print("\n📖 Lecture de la solution existante depuis le fichier...")
excel_solution = ExcelSolution(r"./input_garde_2.xlsx")
solution = excel_solution.read_solution()
print("✅ Solution lue avec succès :")
print(solution)

print("\n⌛ Recherche des créneaux bloqués...")
garde_bloques = excel_solution.compute_blocked_gardes()
astreinte_bloques = excel_solution.compute_blocked_astreintes()

garde_bloques = {(i, datetime_to_string(voeux.creneaux[i])): v for i, v in garde_bloques.items()}
astreinte_bloques = {(i, datetime_to_string(voeux.creneaux[i])): v for i, v in astreinte_bloques.items()}

print(f"🔒 Gardes bloquées : {garde_bloques}")
print(f"🔒 Astreintes bloquées : {astreinte_bloques}")
