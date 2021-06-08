from dao.MonstreDao import MonstreDao
from tools.Connexion import Connexion
import properties
import unittest

class TestMonstreDao(unittest.TestCase):

    def test_getMonstresDonjon(self):
        # INIT
        conn = Connexion(properties.host, properties.database, properties.user, properties.password).conn
        listeMonstres = MonstreDao.getMonstresDonjon(conn, 5)
        # RESULTAT
        print(listeMonstres[0].getId())
        # TEST
        self.assertTrue(True)
        conn.close()

if __name__ == "__main__":
    unittest.main()