import psycopg2

class Reset:

    def reset(conn):
        res = []
        cur = conn.cursor()
        try:
            cur.execute("DROP TABLE IF EXISTS Chasseur CASCADE;")
            cur.execute("DROP TABLE IF EXISTS Groupe CASCADE;")
            cur.execute("DROP TABLE IF EXISTS Donjon CASCADE;")
            cur.execute("DROP TABLE IF EXISTS Monstre CASCADE;")
            cur.execute("DROP TABLE IF EXISTS Guilde CASCADE;")
            cur.execute("DROP TABLE IF EXISTS Lieu CASCADE;")
            cur.execute("DROP TABLE IF EXISTS GroupeGuilde CASCADE;")
            cur.execute("DROP TABLE IF EXISTS GroupeChasseur CASCADE;")
            cur.execute("DROP TABLE IF EXISTS ChasseurGuilde CASCADE;")
            cur.execute("DROP SEQUENCE IF EXISTS idChasseur_seq;")
            cur.execute("DROP SEQUENCE IF EXISTS idMonstre_seq;")
            cur.execute("DROP SEQUENCE IF EXISTS idGroupe_seq;")
            cur.execute("DROP SEQUENCE IF EXISTS idLieu_seq;")

            cur.execute("CREATE SEQUENCE idLieu_seq;")
            cur.execute("CREATE TABLE Lieu(idLieu integer NOT NULL DEFAULT nextval('idLieu_seq'::regclass) PRIMARY KEY UNIQUE,typeLieu text,x integer, y integer);")

            cur.execute("CREATE SEQUENCE idMonstre_seq;")
            cur.execute("CREATE TABLE Monstre(idMonstre integer NOT NULL DEFAULT nextval('idMonstre_seq'::regclass) PRIMARY KEY UNIQUE,nom text,classe text,recompense integer,idLieu integer REFERENCES Lieu ON DELETE CASCADE);")


            cur.execute("CREATE SEQUENCE idChasseur_seq;")
            cur.execute("CREATE TABLE Chasseur(idChasseur integer NOT NULL DEFAULT nextval('idChasseur_seq'::regclass) PRIMARY KEY UNIQUE,age integer, nom text,argent integer, idLieu integer REFERENCES Lieu,classe text,salaire int);")

                        CREATE SEQUENCE idGroupe_seq;
                        CREATE TABLE Groupe
                        (
                            idGroupe integer NOT NULL DEFAULT nextval
                            ('idGroupe_seq'::regclass) PRIMARY KEY UNIQUE,
                            idLieu integer REFERENCES Lieu ON DELETE CASCADE,
                            idDonjon integer REFERENCES Lieu(idLieu) ON DELETE CASCADE
                        );


                        CREATE TABLE Guilde
                        (
                            idGuilde integer NOT NULL PRIMARY KEY UNIQUE REFERENCES Lieu(idLieu) ON DELETE CASCADE, 
                            argent integer,
                            recrute boolean
                        );


                        CREATE TABLE GroupeGuilde
                        (
                            idGroupe integer REFERENCES Groupe ON DELETE CASCADE,
                            idGuilde integer REFERENCES Guilde ON DELETE CASCADE
                        ); 

                        CREATE TABLE GroupeChasseur (
                            idGroupe integer REFERENCES Groupe ON DELETE CASCADE,
                            idChasseur integer REFERENCES Chasseur ON DELETE CASCADE
                        ); 

                        CREATE TABLE ChasseurGuilde (
                            idChasseur integer REFERENCES Chasseur ON DELETE CASCADE,
                            idGuilde integer REFERENCES Guilde ON DELETE CASCADE
                        ); ")
        except psycopg2.Error as error:
            raise error
        finally:
            cur.close()
            return res