from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    __abstract__: bool = True

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"
