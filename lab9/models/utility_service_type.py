from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

import models
from models import Base

class UtilityServiceType(Base):
  __tablename__ = "utility_service_type"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]

  def __repr__(self) -> str:
    return f"UtilityServiceType(id={self.id!r}, name={self.name!r})"