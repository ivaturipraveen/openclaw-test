from fastapi import FastAPI

from database import Base, engine
from routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Production Ready FastAPI Auth API")

app.include_router(auth_router)


@app.get("/")
def health_check():
    return {"message": "API is running"}
