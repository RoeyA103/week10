from pydantic import BaseModel, Field

class Contact(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    phone_number: str = Field(min_length=7, max_length=20)


class ContactUpdate(BaseModel):
    first_name: str  = Field(default=None, min_length=1, max_length=50)
    last_name: str  = Field(default=None, min_length=1, max_length=50)
    phone_number: str  = Field(default=None, min_length=7, max_length=20)
