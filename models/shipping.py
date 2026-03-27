from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Shipping(Base):
    __tablename__ = "shipping"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    address = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    order = relationship("Order")
    user = relationship("User")
