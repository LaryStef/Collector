from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Fiat(Base):
    iso: Mapped[str] = mapped_column(String(3), primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(4096))
    volume: Mapped[float] = mapped_column(Float, default=0)

    def __init__(
        self,
        *,
        iso: str,
        name: str,
        description: str,
        volume: float
    ) -> None:
        self.iso = iso
        self.name = name
        self.description = description
        self.volume = volume
