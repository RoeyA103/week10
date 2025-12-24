from fastapi import FastAPI
from interactor import DataInteractor
from schemas import *

dt = DataInteractor()
   

app = FastAPI()

@app.get("/")
def health():
    return {"healthy"}

@app.get("/contacts")
def list_contacts():
    data = dt.get_contacts()
    return data

@app.post("/contacts")
def create_contacts(contact: Contact):
    ms = dt.create_new_contact(contact)
    return ms

@app.put("/contacts/{id}")
def update_contact(id:int,contact:ContactUpdate):
    ms = dt.update_contact(contact_id=id,contact=contact)
    return ms

@app.delete("/contacts/{id}")
def del_contact(id:int):
    ms = dt.del_contact(id)
    return ms