def verifier_solution(solution, metadata, debug=False):
    blocked_gardes, blocked_astreintes = metadata.blocked_gardes, metadata.blocked_astreintes

    # Vérification des contraintes
    for i, (G_i, A_i) in enumerate(solution):

        # Contrainte 1 : Toutes les gardes sont remplies et G_i ≠ A_i
        if G_i is None or A_i is None:
            return False, f"Créneau {i}: garde ou astreinte manquante."
        if G_i == A_i and not (i in blocked_gardes and i in blocked_astreintes):
            return False, f"Créneau {i}: médecin de garde et astreinte identiques ({G_i})."

        # Vérification que G_i est bien un médecin de garde
        if G_i not in metadata.medecin_data.medecins_garde and i not in blocked_gardes:
            return False, f"Créneau {i}: médecin {G_i} n'est pas autorisé à faire des gardes."

        # Vérification que A_i est bien un médecin d'astreinte
        if A_i not in metadata.medecin_data.medecins_astreinte and i not in blocked_astreintes:
            return False, f"Créneau {i}: médecin {A_i} n'est pas autorisé à faire des astreintes."

        # Contrainte 2 : Pas deux gardes de suite par le même médecin
        if i > 0 and solution[i-1][0] == G_i and not (i-1 in blocked_gardes and i in blocked_gardes):
            return False, f"Créneau {i}: même médecin en garde consécutive ({G_i})."

        # Contrainte 3 : Sur le couple (G_i, A_i), un des deux doit être spécialisé
        if G_i not in metadata.medecin_data.specialisation and A_i not in metadata.medecin_data.specialisation and not (i in blocked_gardes and i in blocked_astreintes):
            return False, f"Créneau {i}: ni G_i ({G_i}) ni A_i ({A_i}) ne sont spécialisés."
        
        # Contrainte 4 : Un créneau bloqué ne doit pas changer
        if i in blocked_gardes and G_i != blocked_gardes[i]:
            return False, f"Créneau {i}: médecin de garde bloqué ({blocked_gardes[i]})."
        if i in blocked_astreintes and A_i != blocked_astreintes[i]:
            return False, f"Créneau {i}: médecin d'astreinte bloqué ({blocked_astreintes[i]})."

    return True, "La solution respecte toutes les contraintes."
