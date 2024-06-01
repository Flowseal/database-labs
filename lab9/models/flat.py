from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from models.payment import Payment
else:
  Payment = "Payment"

from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models import Base

class Flat(Base):
  __tablename__ = "flat"
  id: Mapped[int] = mapped_column(primary_key=True)
  number: Mapped[str]
  rooms: Mapped[int]
  square_area: Mapped[float]

  payments: Mapped[List[Payment]] = relationship(
        back_populates="flat", cascade="all, delete-orphan"
  )

  def __repr__(self) -> str:
      return f"Flat(id={self.id!r}, number={self.number!r}, rooms={self.rooms!r}, square_area={self.square_area!r}, payments=({' || '.join(str(self.payments))}))"