from pydantic import BaseModel, Field

class Contact(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    phone_number: str = Field(min_length=7, max_length=20)


class ContactUpdate(BaseModel):
    first_name: str | None = Field(default=None, min_length=1, max_length=50)
    last_name: str | None = Field(default=None, min_length=1, max_length=50)
    phone_number: str | None = Field(default=None, min_length=7, max_length=20)
