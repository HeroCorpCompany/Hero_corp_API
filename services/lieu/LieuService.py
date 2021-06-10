from dao.LieuDao import LieuDao

class LieuService:

    def getListeLieux(conn):
        res = []
        listeLieux = LieuDao.getListeLieux(conn)
        for lieu in listeLieux:
            lieuDict = LieuService.lieuToDict(lieu)
            res.append(lieuDict)
        return res

            
    def lieuToDict(lieu):
        dict = {}
        if lieu != None:
            dict["id"] = lieu.getId()
            dict["type"] = lieu.getType()
            dict["x"] = lieu.getX()
            dict["y"] = lieu.getY()
        return dict

    def getLieu(conn, idLieu):
        pass

    def getListeDonjons(conn):
        pass