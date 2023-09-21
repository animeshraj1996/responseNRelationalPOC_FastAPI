from typing import Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from models.author import Author


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    author_id: int = Field(foreign_key="author.id")
    author: Optional[Author] = Relationship(back_populates="books")
