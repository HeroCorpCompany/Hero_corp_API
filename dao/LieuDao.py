import psycopg2
from metier.lieu.Lieu import Lieu


class LieuDao:

    def getListeLieux(conn):
        res = []
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Lieu;")
            listeTuples = cur.fetchall()
            for c in listeTuples:
                id = c[0]
                lieu = Lieu(id, c[1], c[2], c[3])
                res.append(lieu)
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            print(res)
            return res
    
    def getListeDonjons(conn):
        res = []
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Lieu WHERE typeLieu='Donjon';")
            listeTuples = cur.fetchall()
            for c in listeTuples:
                id = c[0]
                lieu = Lieu(id, c[1], c[2], c[3])
                res.append(lieu)
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res

    def getLieu(conn, idLieu):
        res = None
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Lieu WHERE idLieu={};".format(idLieu))
            tuple = cur.fetchone()
            res = Lieu(tuple[0], tuple[1], tuple[2], tuple[3])
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res