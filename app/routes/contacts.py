from fastapi import APIRouter
from schemas import Contact, ContactUpdate
from interactor import DataInteractor

dti= DataInteractor()

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.get("/")
def list_contacts():
    """Get all contacts"""
    return dti.get_contacts()


@router.post("/")
def create_contact(contact: Contact):
    """Create new contact"""
    return dti.create_new_contact(contact)


@router.put("/{id}")
def update_contact(id: int, contact: ContactUpdate):
    """Update existing contact"""
    return dti.update_contact(contact_id=id, contact=contact)


@router.delete("/{id}")
def del_contact(id: int):
    """Delete contact"""
    return dti.del_contact(id)
