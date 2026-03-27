from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.order import Order
from models.shipping import Shipping
from models.user import User
from schemas.shipping import ShippingCreate, ShippingResponse
from utils.security import get_current_user

router = APIRouter(prefix="/shipping", tags=["shipping"])


@router.post("", response_model=ShippingResponse, status_code=status.HTTP_201_CREATED)
def create_shipping(
    payload: ShippingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    order = (
        db.query(Order)
        .filter(Order.id == payload.order_id, Order.user_id == current_user.id)
        .first()
    )
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    shipping = Shipping(
        order_id=payload.order_id,
        address=payload.address,
        status=payload.status,
        user_id=current_user.id,
    )
    db.add(shipping)
    db.commit()
    db.refresh(shipping)
    return shipping


@router.get("", response_model=list[ShippingResponse])
def list_shipping(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Shipping).filter(Shipping.user_id == current_user.id).all()
