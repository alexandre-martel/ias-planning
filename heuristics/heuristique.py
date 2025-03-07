from heuristics.verif import verifier_solution

def evaluate(solution, metadata, debug=False):
    
    # Vérification de la solution avec les contraintes
    valid, _ = verifier_solution(solution, metadata)
    
    somme_envies = 0
    nb_creneaux = len(solution)
    
    # Initialisation du compteur de gardes pour chaque médecin
    compteur_gardes = {medecin: 0 for medecin in metadata.medecin_data.medecins_garde}

    penalite_creneau = 0

    for j, (medecin_garde, medecin_astreinte) in enumerate(solution):
        # Extraction des vœux pour ce créneau
        envie_garde = metadata.voeux_data[medecin_garde][j][0]   # Vœu pour être de garde
        envie_astreinte = metadata.voeux_data[medecin_astreinte][j][1]  # Vœu pour être d'astreinte
        
        # Si un médecin exprime une volonté de ne pas être de garde (envie_garde < 0), la solution n'est pas valide
        if envie_garde < 0 :
            penalite_creneau += 1000

        if envie_astreinte < 0:
            penalite_creneau += 500
        
        # Pénalité pour deux gardes consécutives par le même médecin
        if j > 0 and solution[j-1][0] == medecin_garde:
            penalite_creneau += 2000
        elif j == 0 and metadata.last_garde == medecin_garde:
            penalite_creneau += 2000
        
        # Calcul des envies pour les gardes et astreintes
        somme_envies += envie_garde + envie_astreinte
        
        # Mise à jour du compteur de gardes pour les médecins de garde
        compteur_gardes[medecin_garde] += 1

    nombre_moyen_gardes = len(solution) / len(metadata.medecin_data.medecins_garde)

    # Ajustement en fonction des vœux de nombre de gardes (ajouter ou retirer des gardes)
    penalite_garde = 0
    for medecin, nombre_gardes in compteur_gardes.items():
        # Le souhait est donné par voeux_nbr_gardes : -1 (moins de gardes), 0 (égal), 1 (plus de gardes)
        ecart_garde = nombre_gardes - nombre_moyen_gardes

        # Pénalités selon les vœux sur le nombre de gardes
        if metadata.medecin_data.voeux_nbr_gardes[medecin] * ecart_garde < 0:  
            # Si le souhait est -1 (moins de gardes) et ecart_garde > 0, ou
            # Si le souhait est 1 (plus de gardes) et ecart_garde < 0
            penalite_garde += abs(ecart_garde)
        elif metadata.medecin_data.voeux_nbr_gardes[medecin] == 0 and abs(ecart_garde) > 2 :
            # Si le souhait est 0 (dans la moyenne) et |ecart_garde| > 2
            penalite_garde += abs(ecart_garde) / 2.

    if debug: 
        print(f"{nombre_moyen_gardes=}")
        print(f"{somme_envies=}")
        print(f"{penalite_garde=}")
        print(f"{penalite_creneau=}")
        print(f"{valid=}")
        

    # Ajustement final de la satisfaction : on soustrait les pénalités liées aux désirs sur le nombre de gardes
    satisfaction_totale = somme_envies * 5 - penalite_garde *3

    # Satisfaction moyenne normalisée
    satisfaction_moyenne = satisfaction_totale / (2. * nb_creneaux)
    
    return satisfaction_moyenne - penalite_creneau - (not valid) * 1000000

def satisfaction(solution, metadata, medecin):
    score = 100
    compteur_gardes = 0

    for j, (medecin_garde, medecin_astreinte) in enumerate(solution):
        if medecin_garde == medecin:
            compteur_gardes += 1
            envie_garde = metadata.voeux_data[medecin_garde][j][0]
            if envie_garde < 0:
                score -= 20
            elif envie_garde == 0:
                score -= 5
        if medecin_astreinte == medecin:
            envie_astreinte = metadata.voeux_data[medecin_astreinte][j][1]
            if envie_astreinte < 0:
                score -= 10
            elif envie_astreinte == 0:
                score -= 2

    nombre_moyen_gardes = len(solution) / len(metadata.medecin_data.medecins_garde)
    ecart_garde = compteur_gardes - nombre_moyen_gardes
    if metadata.medecin_data.voeux_nbr_gardes[medecin] * ecart_garde < 0:
        score -= abs(ecart_garde)
    elif metadata.medecin_data.voeux_nbr_gardes[medecin] == 0 and abs(ecart_garde) > 2:
        score -= abs(ecart_garde) / 2.

    score -= compteur_gardes

    return max(0, min(100, score))
