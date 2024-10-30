from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import Optional
from peewee import *

import database as db
import students as s
import discipline as disc
import cadru_didactic as cd

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.db.connect()
    yield
    db.db.close()
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/academia/professors/{id}")
def read_item(id: int):
    return {"Aici va fi returnat profesorul cu id-ul": id}

@app.get("/api/academia/professors/{id}/lectures")
def read_item(id: int):
    return {"Aici vor fi returnate disciplinele pe care le preda profesorul cu id-ul": id}

@app.get("/api/academia/students/{id}/lectures")
def read_item(id: int):
    return {"Aici vor fi returnate disciplinele la care participa studentul cu id-ul": id}

@app.get("/api/academia/lectures")
async def get_disciplines(
    cod: Optional[str] = None,
    id_titular: Optional[int] =None,
    nume_disciplina: Optional[str] = None,
    an_studiu: Optional[int] = None,
    tip_disciplina: Optional[str] = None,
    categorie_disciplina: Optional[str] = None,
    tip_examinare: Optional[str] = None
):
    return await disc.Disciplina.get_filtered_disciplines(
        cod=cod,
        id_titular=id_titular,
        nume_disciplina=nume_disciplina,
        an_studiu=an_studiu,
        tip_disciplina=tip_disciplina,
        categorie_disciplina=categorie_disciplina,
        tip_examinare=tip_examinare
    )

@app.get("/api/academia/professors")
async def get_filtered_teaching_staff(     id: Optional[int] = None,
                                          nume: Optional[str] = None,
                                          prenume: Optional[str] = None,
                                          email: Optional[str] = None,
                                          grad_didactic: Optional[str] = None,
                                          tip_asociere: Optional[str] = None,
                                          afiliere: Optional[str] = None):
    
    return await cd.CadruDidactic.get_filtered_teaching_staff(
        id=id,
        nume=nume,
        prenume=prenume,
        email=email,
        grad_didactic=grad_didactic,
        tip_asociere=tip_asociere,
        afiliere=afiliere
    )


@app.get("/api/academia/students")
async def get_students(nume: Optional[str] = None, grupa: Optional[str] = None, an_studiu: Optional[int] = None):
    return await s.Student.get_filtered_students(nume=nume, grupa=grupa, an_studiu=an_studiu)