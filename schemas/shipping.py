from pydantic import BaseModel, Field


class ShippingCreate(BaseModel):
    order_id: int = Field(gt=0)
    address: str = Field(min_length=1, max_length=500)
    status: str = Field(default="pending", min_length=1, max_length=50)


class ShippingResponse(BaseModel):
    id: int
    order_id: int
    address: str
    status: str
    user_id: int

    model_config = {"from_attributes": True}
