class Lieu:

    def __init__(self, id, type, x, y):
        self._id = id
        self._type = type
        self._x = x
        self._y = y

    def getId(self):
        return self._id

    def getType(self):
        return self._type

    def getX(self):
        return self._x

    def getY(self):
        return self._y