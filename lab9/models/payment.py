from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from models.flat import Flat
  from models.utility_rate import UtilityRate
else:
  Flat = "Flat"
  UtilityRate = "UtilityRate"

import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models import Base

class Payment(Base):
  __tablename__ = "payment"
  id: Mapped[int] = mapped_column(primary_key=True)
  payment_amount: Mapped[float]
  date: Mapped[datetime.date]

  flat_id: Mapped[int] = mapped_column(ForeignKey("flat.id"))  
  flat: Mapped[Flat] = relationship(back_populates="payments")
  utility_rate_id: Mapped[UtilityRate] = mapped_column(ForeignKey("utility_rate.id"))  
  utility_rate: Mapped[UtilityRate] = relationship()

  def __repr__(self) -> str:
    return f"Payment(id={self.id!r}, payment_amount={self.payment_amount!r}, service_amount={self.service_amount!r}, date={self.date!r}, flat_id={self.flat.id!r}, utility_rate={str(self.utility_rate)!r})"