from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.order import Order
from models.payment import Payment
from models.user import User
from schemas.payment import PaymentCreate, PaymentResponse
from utils.security import get_current_user

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(
    payload: PaymentCreate,
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

    payment = Payment(
        order_id=payload.order_id,
        amount=payload.amount,
        method=payload.method,
        status=payload.status,
        user_id=current_user.id,
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment


@router.get("", response_model=list[PaymentResponse])
def list_payments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Payment).filter(Payment.user_id == current_user.id).all()
