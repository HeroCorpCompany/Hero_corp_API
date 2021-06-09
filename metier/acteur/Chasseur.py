
class Chasseur:

    def __init__(self, id, age, nom, argent, idPosition, classe, salaire, idGuilde = None, idGroupe = None):
        self._id = id
        self._nom = nom
        self._age = age
        self._classe = classe
        self._argent = argent
        self._salaire = salaire
        self._idPosition = idPosition
        self._idGuilde = idGuilde
        self._idGroupe = idGroupe

    def getId(self):
        return self._id

    def getNom(self):
        return self._nom

    def getAge(self):
        return self._age

    def getClasse(self):
        return self._classe

    def getArgent(self):
        return self._argent

    def getSalaire(self):
        return self._salaire

    def getIdPosition(self):
        return self._idPosition

    def getIdGuilde(self):
        return self._idGuilde

    def getIdGroupe(self):
        return self._idGroupe
