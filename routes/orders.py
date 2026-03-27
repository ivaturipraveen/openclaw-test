from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from models.order import Order
from models.user import User
from schemas.order import OrderCreate, OrderResponse
from utils.security import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    payload: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    order = Order(
        item_name=payload.item_name,
        quantity=payload.quantity,
        total_price=payload.total_price,
        user_id=current_user.id,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("", response_model=list[OrderResponse])
def list_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Order).filter(Order.user_id == current_user.id).all()
