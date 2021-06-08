import psycopg2

class Connexion:

    def __init__(self, host, dbName, user, mdp):
        self.conn = psycopg2.connect(host=host, dbname=dbName, user=user, password=mdp)