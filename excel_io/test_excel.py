from excel import Voeux, ExcelSolution

print("📂 Chargement des fichiers de voeux...")
voeux = Voeux(r"./input_garde_1.xlsx", r"./input_astreinte_1.xlsx")
print("✅ Voeux chargés avec succès :")

# Lire la solution existante depuis le fichier Excel
print("\n📖 Lecture de la solution existante depuis le fichier...")
excel_solution = ExcelSolution(r"./input_garde_1.xlsx")
solution = excel_solution.read_solution()
print("✅ Solution lue avec succès :")
print(solution)

print("\n🔧 Modification de la solution...")
solution = [(f"M{i}", "SHA") for i in range(50)] # Exemple de solution modifiée
print(f"📝 Nouvelle solution créée avec {len(solution)} entrées.")

output_path = r"./test_excel.xlsx"

print(f"\n💾 Sauvegarde de la nouvelle solution dans {output_path}...")
excel_solution.write_solution(solution, output_path)
print("✅ Nouvelle solution sauvegardée avec succès.")
