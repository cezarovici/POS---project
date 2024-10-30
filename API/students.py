from peewee import *
import database as db
from typing import Optional
from enum import Enum

class CicluStudii(Enum):
    LICENTA = "Licenta"
    MASTER = "Master"

class Student(db.DbModel):
    id = AutoField(primary_key=True)  
    nume = CharField(70, null=False)
    prenume = CharField(70, null=False)
    email = CharField(100, unique=True) 
    ciclu_studii = CharField(constraints=[Check(f"ciclu_studii IN ('{CicluStudii.LICENTA.value}', '{CicluStudii.MASTER.value}')")], null=False)
    an_studiu = IntegerField(null=False)
    grupa = IntegerField(null=False)

    @classmethod
    async def get_filtered_students(cls, 
                                    id: Optional[int] = None, 
                                    nume: Optional[str] = None,
                                    prenume: Optional[str] = None, 
                                    email: Optional[str] = None,
                                    ciclu_studii: Optional[str] = None,
                                    an_studiu: Optional[int] = None,
                                    grupa: Optional[int] = None):
        query = cls.select()

        if id:
            query = query.where(cls.id == id)
        if nume:
            query = query.where(cls.nume.contains(nume))
        if prenume:
            query = query.where(cls.prenume.contains(prenume))
        if email:
            query = query.where(cls.email == email)
        if ciclu_studii:
            query = query.where(cls.ciclu_studii == ciclu_studii)
        if an_studiu:
            query = query.where(cls.an_studiu == an_studiu)
        if grupa:
            query = query.where(cls.grupa == grupa)

        return [
            {
                "id": student.id,
                "nume": student.nume,
                "prenume": student.prenume,
                "email": student.email,
                "ciclu_studii": student.ciclu_studii,
                "an_studiu": student.an_studiu,
                "grupa": student.grupa
            }
            for student in query
        ]
        
    class Meta:
        table_name = 'student'