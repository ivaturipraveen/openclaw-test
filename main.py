from fastapi import FastAPI

from database import Base, engine
from models.invoice import Invoice  # noqa: F401
from models.order import Order  # noqa: F401
from models.payment import Payment  # noqa: F401
from models.user import User  # noqa: F401
from routes.auth import router as auth_router
from routes.invoices import router as invoices_router
from routes.orders import router as orders_router
from routes.payments import router as payments_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Production Ready FastAPI Auth API")

app.include_router(auth_router)
app.include_router(orders_router)
app.include_router(payments_router)
app.include_router(invoices_router)


@app.get("/")
def health_check():
    return {"message": "API is running"}
