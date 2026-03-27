from pydantic import BaseModel, Field


class InvoiceCreate(BaseModel):
    order_id: int = Field(gt=0)
    amount: float = Field(gt=0)
    status: str = Field(default="unpaid", min_length=1, max_length=50)


class InvoiceResponse(BaseModel):
    id: int
    order_id: int
    amount: float
    status: str
    user_id: int

    model_config = {"from_attributes": True}
