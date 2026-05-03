from db.database import Base
from sqlalchemy.orm import Mapped,mapped_column

class ContentModel(Base):
    __tablename__ = "content"
    id : Mapped[int] = mapped_column(primary_key=True)
    url : Mapped[str]
    path : Mapped[str]