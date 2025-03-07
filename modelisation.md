# Modélisation IAS

## Modélisation du service hospitalier

### Variables

- On modélise le personnel soignant par $P=\{1,..., N\}$

- Soit $NG$ le nombre de médecins qui peuvent faire de la garde (par exemple 15). L'ensemble des médecins de garde est un sous-ensemble de $P$.

- Soit $NA$ nombre de médecins qui peuvent faire de l’astreinte (par exemple 5 ou 3). L'ensemble des médecins d'astreinte est un sous-ensemble de $P$.

- L'ensemble des médecins spécialisés est un sous-ensemble de $P$.

- Soit $Gmax$ le nombre de gardes maximum par mois pour un médecin

- Soit $VG_{ij}$ le vœux de garde pour le créneau $i$ par le médecin $j$ ($1 \leq j \leq N$)
- Soit $VG_{ij}$ le vœux d'astreinte pour le créneau $i$ par le médecin $j$ ($1 \leq j \leq N$)

### Paramètres

Soit $i$ l'indice du créneau de garde ($i > 0$)

On cherche à remplir les listes $G$ et $A$ telles que :

$G_i$ correspond au médecin de garde au créneau $i$ avec ($1 \leq G_i \leq N$)
$A_i$ correspond au médecin d’astreinte au créneau $i$ avec ($1 \leq A_i \leq N$).
### Contraintes
#### Contrainte 1 : Toutes les gardes sont remplies
$$
\forall i, G_i \hspace{0.2cm}\text{existe et}\hspace{0.1cm}\ A_i \hspace{0.1cm}\ \text{existe.}
$$
$$
\forall i, G_i \neq A_i
$$
#### Contrainte 2 : Pas deux gardes de suite par la même personne dans le même service
$$
\forall i, G_i \neq G_{i+1}
$$
#### Contrainte 3 : Sur le couple ($G_i, A_i$), un des deux doit être spécialisé.
Pour satisfaire la contrainte de spécialisation, il faut :
$$
G_i \in \text{specialisation} || A_i \in \text{specialisation}
$$
#### Contrainte 4 : Pour chaque médecin, le nombre de gardes ne doit pas dépasser le nombre max.
$$
\forall j \in [1, N] : \text{Card}(\{i | G_i = j\}) \leq Gmax
$$
### Critère

Notre critère est la satisfaction moyenne des soignants

Pour calculer la satisfaction d'un soignant :
- Si le médecin $j$ a le créneau de garde $i$ : $+VG_{ij}$
- Si le médecin $j$ n'a pas le créneau de garde $i$ : $-VG_{ij}/3$

A compléter...
