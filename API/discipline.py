from peewee import *
from typing import Optional

import database as db
import cadru_didactic as cd

class Disciplina(db.DbModel):
    COD = CharField(10, primary_key=True) 
    id_titular = ForeignKeyField(cd.CadruDidactic, db_column='id_titular', backref='disciplina',lazy_load=False)
    nume_disciplina = CharField(100, null=False)
    an_studiu = IntegerField(null=False)
    tip_disciplina = CharField(20, constraints=[Check("tip_disciplina IN ('Impusa', 'Optionala', 'Liber_Aleasa')")])
    categorie_disciplina = CharField(20, constraints=[Check("categorie_disciplina IN ('Domeniu', 'Specialitate', 'Adiacenta')")])
    tip_examinare = CharField(20, constraints=[Check("tip_examinare IN ('Examen', 'Colocviu')")])

    class Meta:
        table_name = 'disciplina'

    @classmethod
    async def get_filtered_disciplines(cls,
                                       cod: Optional[str] = None,
                                       id_titular: Optional[int] = None,
                                       nume_disciplina: Optional[str] = None,
                                       an_studiu: Optional[int] = None,
                                       tip_disciplina: Optional[str] = None,
                                       categorie_disciplina: Optional[str] = None,
                                       tip_examinare: Optional[str] = None):
        query = cls.select()

        if cod:
            query = query.where(cls.COD == cod)
        if id_titular:
            query = query.where(cls.id_titular == id_titular)
        if nume_disciplina:
            query = query.where(cls.nume_disciplina.contains(nume_disciplina))
        if an_studiu:
            query = query.where(cls.an_studiu == an_studiu)
        if tip_disciplina:
            query = query.where(cls.tip_disciplina == tip_disciplina)
        if categorie_disciplina:
            query = query.where(cls.categorie_disciplina == categorie_disciplina)
        if tip_examinare:
            query = query.where(cls.tip_examinare == tip_examinare)

        return [
            {
                "COD": disciplina.COD,
                "id_titular": disciplina.id_titular if disciplina.id_titular else None,
                "nume_disciplina": disciplina.nume_disciplina,
                "an_studiu": disciplina.an_studiu,
                "tip_disciplina": disciplina.tip_disciplina,
                "categorie_disciplina": disciplina.categorie_disciplina,
                "tip_examinare": disciplina.tip_examinare
            }
            for disciplina in query
        ]
