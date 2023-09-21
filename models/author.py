from typing import List, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select


class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    books: List["Book"] = Relationship(back_populates="author")
