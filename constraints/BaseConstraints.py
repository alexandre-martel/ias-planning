import uuid   

class Constraints:
    def __init__(self, nb_creneaux, ens=[]):
        self.constraints = ens
        self.constraints.sort(key=lambda x: x.priority, reverse=True)
        self.nb_creneaux = nb_creneaux

    def add(self, constraint):
        for existing in self.constraints:
            if constraint.isInConflict(existing):
                if constraint.priority > existing.priority:
                    self.remove(existing)
                else:
                    return
        self.constraints.append(constraint)
        self.constraints.sort(key=lambda x: x.priority, reverse=True)

    def remove(self, constraint):
        self.constraints.remove(constraint)
        self.constraints.sort(key=lambda x: x.priority, reverse=True)

    def __str__(self):
        return str(self.constraints)

class BaseConstraint:
    def __init__(self, name, priority=0):
        self.name = name
        self.priority = priority
        self.uid = uuid.uuid4()

    def __eq__(self, other):
        return self.uid == other.uid

    def __str__(self):
        return self.name + "(" + str(self.uid) + ")"

    def is_satisfied(self, solution, data):
        raise NotImplementedError

    def apply(self, solution, data):
        raise NotImplementedError

class AssignConstraint(BaseConstraint):
    def __init__(self, name, medecin, creneau, astreinte=0, priority=0):
        super().__init__(name, priority)
        self.medecin = medecin
        self.creneau = creneau
        self.estGarde = astreinte == 0

    def is_satisfied(self, solution, data):
        if self.estGarde:
            return solution[self.creneau][0] == self.medecin
        else:
            return solution[self.creneau][1] == self.medecin

    def __str__(self):
        return self.name + "(" + str(self.uid) + ")[" + ("garde" if self.estGarde else "astreinte") + ": " + str(self.medecin) + ", " + str(self.creneau) + "]"

    def apply(self, solution, data):
        if self.estGarde:
            solution[self.creneau] = (self.medecin, solution[self.creneau][1])
        else:
            solution[self.creneau] = (solution[self.creneau][0], self.medecin)

# Global Constraints

class FollowingGardeConstraint(BaseContraint):
    def __init__(self, name, priority=0):
        super().__init__(name, priority)

    def is_satisfied(self, solution, data):
        for i in range(len(solution) - 1):
            if solution[i][0] == solution[i+1][0]:
                return False
        return True

class MaxGardeConstraint(BaseContraint):
    def __init__(self, name, medecin, max_garde, priority=0):
        super().__init__(name, priority)
        self.medecin = medecin
        self.max_garde = max_garde

    def is_satisfied(self, solution, data):
        return sum([1 for i in range(len(solution)) if solution[i][0] == self.medecin]) <= self.max_garde

class AllGardeAssignedConstraint(BaseConstraint):
    def __init__(self, name, priority=0):
        super().__init__(name, priority)

    def is_satisfied(self, solution, data):
        return all([solution[i][0] != None for i in range(len(solution))])

class AllAstreinteAssignedConstraint(BaseConstraint):
    def __init__(self, name, priority=0):
        super().__init__(name, priority)

    def is_satisfied(self, solution, data):
        return all([solution[i][1] != None for i in range(len(solution))])


if __name__ == "__main__":
    c1 = AssignConstraint("c1", "medecin1", 0, priority=10)
    