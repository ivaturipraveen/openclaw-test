from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="unpaid")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    order = relationship("Order")
    user = relationship("User")
