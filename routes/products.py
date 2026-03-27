from fastapi import APIRouter

router = APIRouter(prefix="", tags=["products"])


@router.get("/products")
def list_products():
    return [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Mouse", "price": 29.99},
        {"id": 3, "name": "Keyboard", "price": 79.99},
    ]
