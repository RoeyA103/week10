from pydantic import BaseModel

class Contact(BaseModel):
    first_name:str
    last_name:str
    phone_number:str

class ContactUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None 