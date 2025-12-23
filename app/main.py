from fastapi import FastAPI
from pydantic import BaseModel
from interactor import DataInteractor

dt = DataInteractor()

class Contact(BaseModel):
    first_name:str
    last_name:str
    phone_number:str

class ContactUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None    

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