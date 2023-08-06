from fastapi import FastAPI
from manage_payables_receivables.routers import manage_payables_receivables as man


app = FastAPI(
    title="API Testing",
    description="API for testing with FastAPI",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json"  # URL para a especificação OpenAPI
)


@app.get("/")
def index():
    return {"message": "Hello World"}


app.include_router(man.router)