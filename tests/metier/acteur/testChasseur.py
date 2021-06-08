from metier.acteur.Chasseur import Chasseur
import unittest

class TestChasseur(unittest.TestCase):

    def test_getId(self):
        # INIT
        attendu = 12
        chasseur = Chasseur(attendu, "Souli", 22, "A", 3500, 1200, None)
        # RESULTAT
        resultat = chasseur.getId()
        # TEST
        self.assertEqual(attendu, resultat)

    def test_getNom(self):
        # INIT
        attendu = "Souli"
        chasseur = Chasseur(12, attendu, 22, "A", 3500, 1200, None)
        # RESULTAT
        resultat = chasseur.getNom()
        # TEST
        self.assertEqual(attendu, resultat)

if __name__ == "__main__":
    unittest.main()