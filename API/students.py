from peewee import *
import database as db
from typing import Optional

class Student(db.DbModel):
    id_student = IntegerField().primary_key
    nume = CharField(70)
    prenume = CharField(70)
    grupa = CharField(50)
    an_studiu = IntegerField()

    @classmethod
    async def get_filtered_students(cls, nume: Optional[str] = None, grupa: Optional[str] = None, an_studiu: Optional[int] = None):
            # Construim query-ul
            query = cls.select()
            
            if nume:
                query = query.where(cls.nume.contains(nume))
            if grupa:
                query = query.where(cls.grupa == grupa)
            if an_studiu:
                query = query.where(cls.an_studiu == an_studiu)
            
            # Returnăm lista de studenți cu filtrare aplicată
            return [
                {
                    "id_student": student.id_student,
                    "nume": student.nume,
                    "prenume": student.prenume,
                    "grupa": student.grupa,
                    "an_studiu": student.an_studiu
                }
                for student in query
            ]