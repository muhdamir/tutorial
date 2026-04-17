from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    blog: Mapped[list['Blog']] = relationship('Blog', back_populates='user')


class Blog(Base):
    __tablename__ = 'blog'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(ForeignKey('user.name'), nullable=False)

    user: Mapped['User'] = relationship('User', back_populates='blog')
