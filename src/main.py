from fastapi import FastAPI
from src.infrastructure.api.routes import router

app = FastAPI(title="User CRUD API", version="1.0.0")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the User CRUD API. Go to /docs for Swagger documentation."}
