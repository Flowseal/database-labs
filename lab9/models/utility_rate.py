from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from models.utility_service_type import UtilityServiceType
else:
  UtilityServiceType = "UtilityServiceType"

import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models import Base

class UtilityRate(Base):
  __tablename__ = "utility_rate"
  id: Mapped[int] = mapped_column(primary_key=True)
  date_start: Mapped[datetime.date]
  date_end: Mapped[datetime.date]
  price: Mapped[float]

  service_type_id: Mapped[int] = mapped_column(ForeignKey("utility_service_type.id"))
  service_type: Mapped[UtilityServiceType] = relationship()

  def __repr__(self) -> str:
    return f"UtilityRate(id={self.id!r}, date_start={self.date_start!r}, date_end={self.date_end!r}, price={self.price!r}), service_type={self.service_type.name!r})"