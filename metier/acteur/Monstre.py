
class Monstre:

    def __init__(self, id, nom, classe, recompense, idDonjon):
        self._id = id
        self._nom = nom
        self._classe = classe
        self._recompense = recompense
        self._idDonjon = idDonjon

    def getId(self):
        return self._id
    
    def getNom(self):
        return self._nom

    def getClasse(self):
        return self._classe

    def getRecompense(self):
        return self._recompense

    def getIdDonjon(self):
        return self._idDonjon