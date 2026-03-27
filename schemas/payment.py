from pydantic import BaseModel, Field


class PaymentCreate(BaseModel):
    order_id: int = Field(gt=0)
    amount: float = Field(gt=0)
    method: str = Field(min_length=1, max_length=100)
    status: str = Field(default="pending", min_length=1, max_length=50)


class PaymentResponse(BaseModel):
    id: int
    order_id: int
    amount: float
    method: str
    status: str
    user_id: int

    model_config = {"from_attributes": True}
