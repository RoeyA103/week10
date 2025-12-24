from fastapi import FastAPI
from routes.contacts import router as contacts_router
from schemas import *


app = FastAPI()

@app.get("/")
def health():
    return {"healthy"}

app.include_router(contacts_router)
