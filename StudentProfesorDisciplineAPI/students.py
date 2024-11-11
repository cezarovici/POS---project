from peewee import *
from typing import Optional
from enum import Enum
from fastapi_hypermodel import FrozenDict, HALFor, HALHyperModel, HALLinks
import database as db

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

    def generate_student_links(self) -> HALLinks:
        return HALLinks(
            self=HALFor("get_student", {"id": self.id}),
            update=HALFor("update_student", {"id": self.id}),
            delete=HALFor("delete_student", {"id": self.id})
        )

    @classmethod
    async def get_filtered_students(cls, id: Optional[int] = None, nume: Optional[str] = None,
                                    prenume: Optional[str] = None, email: Optional[str] = None,
                                    ciclu_studii: Optional[str] = None, an_studiu: Optional[int] = None,
                                    grupa: Optional[int] = None):
        query = cls.select()
        
        # Apply filters if parameters are provided
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

        # Return a list of filtered student data with HATEOAS links
        return [
            {
                "id": student.id,
                "nume": student.nume,
                "prenume": student.prenume,
                "email": student.email,
                "ciclu_studii": student.ciclu_studii,
                "an_studiu": student.an_studiu,
                "grupa": student.grupa,
                "links": student.generate_student_links()  
            }
            for student in query
        ]
    
    class Meta:
        table_name = 'student'
