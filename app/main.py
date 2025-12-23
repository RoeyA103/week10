from fastapi import FastAPI


app = FastAPI()

@app.get("/health")
def health():
    return {"healthy"}

@app.get("/contacts")
def list_contacts():
    data = get_contacts()
    return data

@app.post("/contacts")
def create_contacts():
    pass

@app.put("/contacts/{id}")
def update_contact(id:int):
    pass

@app.delete("/contacts/{id}")
def del_contact(id:int):
    pass