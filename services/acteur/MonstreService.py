from dao.MonstreDao import MonstreDao

class MonstreService:

    def getMonstresDonjon(conn, idDonjon):
        res = []
        listeMonstres = MonstreDao.getMonstresDonjon(conn, idDonjon)
        for monstre in listeMonstres:
            monstreDict = MonstreService.monstreToDict(monstre)
            res.append(monstreDict)
        return res

    def monstreToDict(monstre):
        dict = {}
        dict["id"] = monstre.getId()
        dict["nom"] = monstre.getNom()
        dict["classe"] = monstre.getClasse()
        dict["recompense"] = monstre.getRecompense()
        dict["idDonjon"] = monstre.getIdDonjon()
        return dict
