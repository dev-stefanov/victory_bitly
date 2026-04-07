from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class BaseModel(DeclarativeBase):
    ...

class LinkModel(BaseModel):
    __tablename__ = 'links'
    short_id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column()
    count: Mapped[int] = mapped_column(default=0)
    
