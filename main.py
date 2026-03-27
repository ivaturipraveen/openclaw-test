from fastapi import FastAPI

from database import Base, engine
from models.order import Order  # noqa: F401
from models.user import User  # noqa: F401
from routes.auth import router as auth_router
from routes.orders import router as orders_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Production Ready FastAPI Auth API")

app.include_router(auth_router)
app.include_router(orders_router)


@app.get("/")
def health_check():
    return {"message": "API is running"}
