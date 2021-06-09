import uvicorn
from fastapi import FastAPI
from services.acteur.ChasseurService import ChasseurService
from services.lieu.LieuService import LieuService
from services.lieu.GuildeService import GuildeService
from services.acteur.MonstreService import MonstreService
from tools.Connexion import Connexion
import properties as p

app = FastAPI()

conn = Connexion(p.host, p.database, p.user, p.password).conn


@app.get("/")
def root():
    return {"result": "ok"}

@app.get("/chasseurs")
def getChasseurs():
    return ChasseurService.getListeChasseurs(conn)

@app.get("/lieux")
def getLieux():
    return LieuService.getListeLieux(conn)

@app.get("/guildes/{idGuilde}")
def getGuilde(idGuilde):
    return GuildeService.getGuilde(conn, idGuilde)

@app.get("/monstres/{idDonjon}")
def getMonstres(idDonjon):
    return MonstreService.getMonstresDonjon(conn, idDonjon)

@app.get("/chasseurs/guilde/{idGuilde}")
def getChasseursGuilde(idGuilde):
    pass

@app.get("/chasseurs/lieu/{idLieu}")
def getChasseursLieu(idLieu):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
