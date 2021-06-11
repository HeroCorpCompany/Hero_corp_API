from dao.LieuDao import LieuDao
from dao.ChasseurDao import ChasseurDao
from dao.MonstreDao import MonstreDao
from dao.GuildeDao import GuildeDao
from services.acteur.ChasseurService import ChasseurService
from services.acteur.MonstreService import MonstreService
from services.lieu.GuildeService import GuildeService
from services.lieu.LieuService import LieuService
from dao.StatsDao import StatsDao

class WorldService:

    def getAll(conn):
        listeLieux = LieuDao.getListeLieux(conn)
        lieuxFinal = []
        listeChasseurs = ChasseurDao.getListeChasseurs(conn)
        chasseursFinal = []
        listeMonstres = MonstreDao.getListeMonstres(conn)
        monstresFinal = []
        listeGuildes = GuildeDao.getListeGuildes(conn)
        guildesFinal = []
        stats = StatsDao.getStats(conn)
        res = {}
        for lieu in listeLieux:
            lieuxFinal.append(LieuService.lieuToDict(lieu))
        for chasseur in listeChasseurs:
            chasseursFinal.append(ChasseurService.chasseurToDict(chasseur))
        for monstre in listeMonstres:
            monstresFinal.append(MonstreService.monstreToDict(monstre))
        for guilde in listeGuildes:
            guildesFinal.append(GuildeService.guildeToDict(guilde))
        res["lieux"] = lieuxFinal
        res ["chasseurs"] = chasseursFinal
        res["monstres"] = monstresFinal
        res["guildes"] = guildesFinal
        res["stats"] = stats
        return res
