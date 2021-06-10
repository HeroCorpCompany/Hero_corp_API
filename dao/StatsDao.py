import psycopg2

class StatsDao:

    def getStats(conn):
        res = {}
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM Stats;")
            tuple = cur.fetchone()
            res["temps"] = tuple[1]
            res["nbChasseurs"] = tuple[2]
            res["nbDonjons"] = tuple[3]
            res["nbGuildes"] = tuple[4]
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res