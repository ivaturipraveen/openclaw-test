from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    item_name: str = Field(min_length=1, max_length=255)
    quantity: int = Field(gt=0)
    total_price: float = Field(gt=0)


class OrderResponse(BaseModel):
    id: int
    item_name: str
    quantity: int
    total_price: float
    user_id: int

    model_config = {"from_attributes": True}
