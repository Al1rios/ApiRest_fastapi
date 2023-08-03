from fastapi import FastAPI
from manage_payables_receivables.routers import manage_payables_receivables as man


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}

app.include_router(man.router)