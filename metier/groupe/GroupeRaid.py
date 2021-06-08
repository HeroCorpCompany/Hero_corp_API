class GroupeRaid:

    def __init__(self, id, idPosition, idCible, idGuilde = None):
        self._id = id
        self._idPosition = idPosition
        self._idCible = idCible
        self._idGuilde = idGuilde

    def getId(self):
        return self._id

    def getIdPosition(self):
        return self._idPosition

    def getIdCible(self):
        return self._idCible

    def getIdGuilde(self):
        return self._idGuilde