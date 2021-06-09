from dao.ChasseurDao import ChasseurDao

class ChasseurService:

    def getListeChasseurs(conn):
        res = []
        listeChasseurs = ChasseurDao.getListeChasseurs(conn)
        for chasseur in listeChasseurs:
            chasseurDict = ChasseurService.chasseurToDict(chasseur)
            res.append(chasseurDict)
        return res

    def getChasseursGuilde(conn, idGuilde):
        listeChasseurs = ChasseurDao.getChasseursGuilde(conn, idGuilde)
        res = []
        for chasseur in listeChasseurs:
            chasseurDict = ChasseurService.chasseurToDict(chasseur)
            res.append(chasseurDict)
        return res

    def getChasseursLieu(conn, idLieu):
        listeChasseurs = ChasseurDao.getChasseursLieu(conn, idLieu)
        res = []
        for chasseur in listeChasseurs:
            chasseurDict = ChasseurService.chasseurToDict(chasseur)
            res.append(chasseurDict)
        return res

    
    def chasseurToDict(chasseur):
        dict = {}
        dict["id"] = chasseur.getId()
        dict["nom"] = chasseur.getNom()
        dict["age"] = chasseur.getAge()
        dict["argent"] = chasseur.getArgent()
        dict["idPosition"] = chasseur.getIdPosition()
        dict["classe"] = chasseur.getClasse()
        dict["salaire"] = chasseur.getSalaire()
        dict["idGuilde"] = chasseur.getIdGuilde()
        dict["idGroupe"] = chasseur.getIdGroupe()
        return dict