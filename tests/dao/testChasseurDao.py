from dao.ChasseurDao import ChasseurDao
from tools.Connexion import Connexion
import properties
import unittest

class TestChasseurDao(unittest.TestCase):

    def test_getListeChasseurs(self):
        # INIT
        conn = Connexion(properties.host, properties.database, properties.user, properties.password).conn
        listeChasseurs = ChasseurDao.getListeChasseurs(conn)
        # RESULTAT
        print(listeChasseurs[0].getNom())
        # TEST
        self.assertTrue(True)
        conn.close()

if __name__ == "__main__":
    unittest.main()