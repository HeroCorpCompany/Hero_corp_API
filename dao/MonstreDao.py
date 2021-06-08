import psycopg2
from metier.acteur.Monstre import Monstre

class MonstreDao:

    def getMonstresDonjon(conn, idDonjon):
        res = []
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Monstre WHERE idLieu={};".format(idDonjon))
            listeTuples = cur.fetchall()
            for c in listeTuples:
                id = c[0]
                monstre = Monstre(id, c[1], c[2], c[3], c[4])
                res.append(monstre)
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res