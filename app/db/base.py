from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,declared_attr


class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True)