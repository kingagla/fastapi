from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String

from db.database import Base


class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)  # will be hashed to do not have visibility even in DB
    items = relationship(
        "DbArticle", back_populates="user"
    )  # backpopulates = to which column is connected


class DbArticle(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DBUser", back_populates="items")
