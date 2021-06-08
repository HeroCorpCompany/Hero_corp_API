

from tools.Connexion import Connexion
import psycopg2
from metier.acteur.Chasseur import Chasseur

class ChasseurDao:

    def getListeChasseurs(conn):
        res = []
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Chasseur;")
            listeTuples = cur.fetchall()
            for c in listeTuples:
                id = c[0]
                try:    
                    idGuilde = ChasseurDao.isInGuilde(conn, id)
                except:
                    idGuilde = None
                try:
                    idGroupe = ChasseurDao.isInGroupe(conn, id)
                except:
                    idGroupe = None
                chasseur = Chasseur(id, c[1], c[2], c[3], c[4], c[5], c[6], idGuilde, idGroupe)
                res.append(chasseur)
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res

    def isInGuilde(conn, id):
        res = None
        cur = conn.cursor()
        try:
            cur.execute("SELECT idGuilde FROM ChasseurGuilde WHERE idChasseur={};".format(id))
            res = cur.fetchone()[0]
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res

    def isInGroupe(conn, id):
        res = None
        cur = conn.cursor()
        try:
            cur.execute("SELECT idGroupe FROM GroupeChasseur WHERE idChasseur={};".format(id))
            res = cur.fetchone()[0]
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res
