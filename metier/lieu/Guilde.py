
class Guilde:

    def __init__(self, id, argent, recrute):
        self._id = id
        self._argent = argent
        self._recrute = recrute

    def getId(self):
        return self._id

    def getArgent(self):
        return self._argent

    def isRecruting(self):
        return self._recrute