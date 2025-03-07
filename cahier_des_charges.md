# 1. Tableaux

## 1.1 Pour la création des premiers tableaux d'un semestre 

Les tableaux sont construits de manière séquentielle, celui des gardes puis celui des astreintes ou l'inverse. Les contraintes d'un tableau peuvent imposer de modifier l'autre. 

### En entrée : 
- le tableau vide. cf fichier "À remplir par semestre"
- le tableau des disponibilités "Tableau des disponibilités..."
- le tableau des contraintes (nombre de gardes min, max, cible ...)

### En sortie : 
le tableau calculé. Cf fichier "Résultat après calcul"

Les tableaux sont construits mois par mois avec un contrôle de l'étalement et du nombre de gardes ou d'astreintes par mois et par semestre, ainsi que du contrôle de la présence d'au moins 1 CCV par date. 

Les tableaux des disponibilités sont codés ainsi : `<0=impossible, 0=si et seulement si indispensable pour lever un blocage, >0=possible` avec gradation possible pour les valeurs >0. Plus la valeur est élevée, plus la date est souhaitée :
- Cf fichier "Tableau des disponibilités pour Astreintes"
- Cf fichier "Tableau des disponibilités pour Gardes"

### Fichiers utilisés pour réaliser le calcul manuel
- Cf fichier "Synthèse utilisée pour le calcul manuel des Astreintes"
- Cf fichier "Synthèse utilisée pour le calcul manuel des Gardes"

## 1.2 Pour les modifications des tableaux 
	
### En entrée : 
- le tableau calculé
- la ou les dates à modifier
- le tableau des disponibilités
- le tableau des contraintes (nombre de gardes min, max, cible ...)

### En sortie : 
le nouveau tableau calculé. Cf fichier "Résultat après calcul" 	

## 1.3 ATTENTE du projet pour la partie algorithmique : 

Proposer un démonstrateur en ligne de commande. 

### En entrée :
le tableau vide ou déjà rempli, le tableau des disponibilités, un tableau d'expression des contraintes (quotas, étalement, "au moins 1 CCV"...), un tableau des dates à modifier....

### En sortie :
un tableau proposant une répartition des gardes et astreintes.

## 1.4 GENERALISATION 
Extrapolation à la gestion de plusieurs tableaux pour plusieurs services (sites) pour plusieurs établissements avec des intersections entre équipes vides ou non.

# 2. Problème en amont : 
Capture et actualisation des disponibilités (IHM)

# 3. Problème en aval : 
Diffusion des attributions, mise à jour des disponibilités, proposition des modifications.
