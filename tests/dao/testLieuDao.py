from dao.LieuDao import LieuDao
from tools.Connexion import Connexion
import properties
import unittest

class TestLieuDao(unittest.TestCase):

    def test_getListeLieux(self):
        # INIT
        conn = Connexion(properties.host, properties.database, properties.user, properties.password).conn
        listeLieux = LieuDao.getListeLieux(conn)
        # RESULTAT
        print(listeLieux[0].getType())
        # TEST
        self.assertTrue(True)
        conn.close()

    def test_getListeDonjons(self):
        # INIT
        conn = Connexion(properties.host, properties.database, properties.user, properties.password).conn
        listeDonjons = LieuDao.getListeDonjons(conn)
        # RESULTAT
        print(listeDonjons[0].getType())
        # TEST
        self.assertTrue(True)
        conn.close()

    def test_getLieu(self):
        # INIT
        conn = Connexion(properties.host, properties.database, properties.user, properties.password).conn
        lieu = LieuDao.getLieu(conn, 3)
        # RESULTAT
        print(lieu.getType())
        # TEST
        self.assertTrue(True)
        conn.close()

if __name__ == "__main__":
    unittest.main()