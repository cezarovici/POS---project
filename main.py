from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/lectures/{id}")
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
    return {"Aici vor fi returnate disciplinele la care participa cu id-ul": id}

@app.get("/api/academia/lectures?page={page_number}/items_per_page={items_per_page}")
def read_item(page_number: int, items_per_page: int):
    return f"Aici vor fi returnate toate disciplinele de pe pagina {page_number} cu {items_per_page} elemente pe pagina"

