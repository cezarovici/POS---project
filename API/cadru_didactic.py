from peewee import *
import database as db
from typing import Optional
from enum import Enum

class GradDidactic(Enum):
    ASISTENT = "Asistent"
    SEF_LUCRARI = "Sef Lucrari"
    CONFERENTIAR = "Conferentiar"
    PROFESOR = "Profesor"

class TipAsociere(Enum):
    TITULAR = "Titular"
    ASOCIAT = "Asociat"
    EXTERN = "Extern"

class CadruDidactic(db.DbModel):
    id = AutoField(primary_key=True)
    nume = CharField(70, null=False)
    prenume = CharField(70, null=False)
    email = CharField(100, unique=True)

    grad_didactic = CharField(
        constraints=[
            Check(f"grad_didactic IN ('{GradDidactic.ASISTENT.value}', '{GradDidactic.SEF_LUCRARI.value}', '{GradDidactic.CONFERENTIAR.value}', '{GradDidactic.PROFESOR.value}')")
        ],
        null=False
    )
    
    tip_asociere = CharField(
        constraints=[
            Check(f"tip_asociere IN ('{TipAsociere.TITULAR.value}', '{TipAsociere.ASOCIAT.value}', '{TipAsociere.EXTERN.value}')")
        ],
        null=False
    )
    
    afiliere = CharField(255, null=True)  

    @classmethod
    async def get_filtered_teaching_staff(cls,
                                          id: Optional[int] = None,
                                          nume: Optional[str] = None,
                                          prenume: Optional[str] = None,
                                          email: Optional[str] = None,
                                          grad_didactic: Optional[str] = None,
                                          tip_asociere: Optional[str] = None,
                                          afiliere: Optional[str] = None):
        query = cls.select()

        if id:
            query = query.where(cls.id == id)
        if nume:
            query = query.where(cls.nume.contains(nume))
        if prenume:
            query = query.where(cls.prenume.contains(prenume))
        if email:
            query = query.where(cls.email == email)
        if grad_didactic:
            query = query.where(cls.grad_didactic == grad_didactic)
        if tip_asociere:
            query = query.where(cls.tip_asociere == tip_asociere)
        if afiliere:
            query = query.where(cls.afiliere.contains(afiliere))

        return [
            {
                "id": staff.id,
                "nume": staff.nume,
                "prenume": staff.prenume,
                "email": staff.email,
                "grad_didactic": staff.grad_didactic,
                "tip_asociere": staff.tip_asociere,
                "afiliere": staff.afiliere
            }
            for staff in query
        ]

    class Meta:
        table_name = 'cadru_didactic'
