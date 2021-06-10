from dao.GuildeDao import GuildeDao

class GuildeService:

    def getListeGuildes(conn):
        pass

    def getGuilde(conn, idGuilde):
        guilde = GuildeDao.getGuilde(conn, idGuilde)
        guildeDict = GuildeService.guildeToDict(guilde)
        return guildeDict

    def guildeToDict(guilde):
        dict = {}
        if guilde != None:
            dict["id"] = guilde.getId()
            dict["argent"] = guilde.getArgent()
            dict["recrute"] = guilde.isRecruting()
        return dict