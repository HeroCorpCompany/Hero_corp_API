import psycopg2
from metier.lieu.Guilde import Guilde

class GuildeDao:

    def getListeGuildes(conn):
        res = []
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Guilde;")
            listeTuples = cur.fetchall()
            for c in listeTuples:
                guilde = Guilde(c[0], c[1], c[2])
                res.append(guilde)
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res

    def getGuilde(conn, id):
        res = None
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Guilde WHERE idGuilde={};".format(id))
            tuple = cur.fetchone()
            res = Guilde(tuple[0], tuple[1], tuple[2])
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res