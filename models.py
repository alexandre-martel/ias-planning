import uuid

class MedecinData :
    def __init__(self, medecins_garde, medecins_astreinte, specialisation, Gmax, voeux_nbr_gardes):
        self.medecins_garde = list(set(medecins_garde))
        self.medecins_astreinte = list(set(medecins_astreinte))
        self.specialisation = specialisation
        self.Gmax = Gmax
        self.voeux_nbr_gardes = voeux_nbr_gardes

    def __str__(self):
        return "MedecinData[garde:" + str(self.medecins_garde) + ", astreinte:" + str(self.medecins_astreinte) + ", spe:" + str(self.specialisation) + ", Gmax:" + str(self.Gmax) + ", voeux_nbr_gardes:" + str(self.voeux_nbr_gardes) + "]"

class Medecin :
    def __init__(self, trigramme, specialisation=0):
        self.uid = uuid.uuid4()
        self.trigramme = trigramme
        self.specialisation = specialisation

    def __str__(self):
        return self.trigramme + "(spe:" + str(self.specialisation) + ")"
    

class Metadata:
    def __init__(self, medecin_data, voeux_data=None, blocked_gardes=None, blocked_astreintes=None, last_garde=None):
        self.medecin_data = medecin_data
        self.voeux_data = voeux_data
        self.blocked_gardes = blocked_gardes
        self.blocked_astreintes = blocked_astreintes
        self.last_garde = last_garde
    