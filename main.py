from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/academia/lectures/{id}")
def read_item(id: int):
    return {"Aici va fi returnata disciplina cu id-ul": id}

@app.get("/api/academia/students/{id}")
def read_item(id: int):
    return {"Aici va fi returnat studentul cu id-ul": id}

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
def read_item(page_number: Optional[int] = None, items_per_page: Optional[int] = None):
    if page_number and not items_per_page:
        return f"Aici vor fi returnate toate disciplinele de la pagina"
    if not page_number and items_per_page:
        return f"Aici vor fi returnate toate disciplinele cate {items_per_page} pe pagina"
    if not page_number and not items_per_page:
       return f"Aici vor fi returnate toate disciplinele"
    else:
        return f"Aici vor fi returnate disciplinele de la pagina {page_number} cu {items_per_page} per pagina"

@app.get("/api/academia/professors")
def read_item(name: Optional[str] = None, acad_rank: Optional[str] = None):
    if name and not acad_rank:
        return f"Aici va fi returnat profesorii care au numele {name}"
    if acad_rank and not name:
        return f"Aici vor fi returnati profesorii cu gradul {acad_rank}"
    if acad_rank and name:
        return f"Aici vor fi profesorii cu gradul {acad_rank} si numele {name}"
    else:
        return f"Aici vor fi afisati toti profesorii"
