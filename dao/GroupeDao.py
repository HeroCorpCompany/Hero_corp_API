import psycopg2
from metier.groupe.GroupeRaid import GroupeRaid

class GroupeDao:

    def getListeGroupes(conn):
        res = []
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Groupe;")
            listeTuples = cur.fetchall()
            for c in listeTuples:
                id = c[0]
                try:
                    idGuilde = GroupeDao.hasGuilde(id)
                except:
                    idGuilde = None
                groupe = GroupeRaid(id, c[1], c[2], idGuilde)
                res.append(groupe)
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res

    def hasGuilde(conn, id):
        res = None
        cur = conn.cursor()
        try:
            cur.execute("SELECT idGuilde FROM GroupeGuilde WHERE idGroupe={};".format(id))
            res = cur.fetchone()[0]
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res
    
    def getGroupe(conn, id):
        res = None
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Groupe WHERE idGroupe={};".format(id))
            tuple = cur.fetchone()
            id = tuple[0]
            try:
                idGuilde = GroupeDao.hasGuilde(id)
            except:
                idGuilde = None
            res = GroupeRaid(id, tuple[1], tuple[2], None)
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res