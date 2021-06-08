from tools.Connexion import Connexion
from dao.GroupeDao import GroupeDao
import properties
import unittest

class TestLieuDao(unittest.TestCase):

    def test_getListeGroupes(self):
        # INIT
        conn = Connexion(properties.host, properties.database, properties.user, properties.password).conn
        listeGroupes = GroupeDao.getListeGroupes(conn)
        # RESULTAT
        print(listeGroupes[0].getIdCible())
        # TEST
        self.assertTrue(True)
        conn.close()

    def test_getGroupe(self):
        # INIT
        conn = Connexion(properties.host, properties.database, properties.user, properties.password).conn
        groupe = GroupeDao.getGroupe(conn, 8)
        # RESULTAT
        print(groupe.getIdCible())
        # TEST
        self.assertTrue(True)
        conn.close()

    def test_hasGuilde(self):
        # INIT
        conn = Connexion(properties.host, properties.database, properties.user, properties.password).conn
        idGuilde = GroupeDao.hasGuilde(conn, 7)
        # RESULTAT
        print(idGuilde)
        # TEST
        self.assertTrue(True)
        conn.close()

if __name__ == "__main__":
    unittest.main()