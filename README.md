# IAS
IAS 2024 est un projet de génération de planning de garde en service hosptalier, réalisé dans le cadre de l'électif *Intelligence Artificielle et Santé* de la deuxième année du cursus ingénieur de l'Ecole Centrale de Lille. L'équipe du projet est composée de AZARIOUH Salwa, CHAQUIQ EL BADRE Othman, DROUET Baptiste, MAREMBERT David, MARTEL Alexandre et MOUSTACHE Mohamed. 

Vous pouvez trouver ici le [cahier des charges](cahier_des_charges.md) de notre projet fourni par un médecin du CHU de Lille qui intervient sur l'électif, ainsi que [notre rapport](rapport.pdf).

## Prérequis avant le lancement

### Installation
Sur Windows :
```
setup.bat
```

Sur Linux :
```sh
./setup.sh
```

### Documents à fournir
* Importez le fichier des [médecins](medecins.xlsx) qui contient la liste des médecins disponibles dans le service ainsi que leurs caractéristiques: garde (oui ou non), astreinte (oui ou non), CCV (oui ou non) ainsi qu'une valeur entre -1 et 1 appelé "Voeux". Les Voeux correspondent aux souhaits des médecin d'avoir plus (+1), moins (-1) ou autant (0) de garde que la moyenne. 

* Importez les tableau excel des voeux de garde et d'astreinte sans créneaux attribués. Tous les créneaux pré-remplis à la main consitueront des créneaux bloqués, qui ne seront pas modifiés par l'algorithme, et permettent ainsi de forcer des créneaux convenus à l'avance au sein du personnel soignant, même si ceux-ci ne respectent pas les contraintes, en cas de situation exceptionnelle par exemple.

### Paramètres à définir
Il est possible de [configurer l'algorithme](config.properties). Parmi les propriétés, il y a :
* `begin` : la date de début du remplissage du planning au format `YYYY-MM-DD`
* `end` : la date de fin du remplissage du planning au format `YYYY-MM-DD`
* `gardes_max` : le nombre de gardes maximal par medecin
* `last_garde` : le medecin en garde dans le créneau avant begin (afin d'assurer la continuité des contraintes entre les périodes)

## Lancement du programme
Sur Windows :
```
run.bat
```

Sur Linux :
```sh
./run.sh
```

La lecture du script [run](run.py) permet une visualisation globale de notre démarche : à partir des documents importés précédemment ([médecins](medecins.xlsx), [tableaux de voeux](...)), il recherche les créneaux bloqués, complète la solution initiale avec un algorithme glouton naïf, affiche le nouveau score, et optimise ce planning avec les algorithmes [recuit-simulé](algos\algo_rs.py), [tabou](algos\algo_tabou.py) et [génétique](algos\aglo_genetique.py) avant d'afficher les nouveaux scores. Run génère alors un planning complet dans une copie du fichier excel. 