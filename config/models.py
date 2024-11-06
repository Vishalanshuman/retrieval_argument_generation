from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from config.database import Base
from passlib.hash import bcrypt as passlib_bcrypt


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=func.now(), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  

    user = relationship("User", back_populates="documents")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False, nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=True)

    documents = relationship("Document", back_populates="user")
    chats = relationship("Chat", back_populates="user")  # Added this relationship

    def verify_password(self, password: str) -> bool:
        return passlib_bcrypt.verify(password, self.hashed_password)


class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=True)

    user = relationship("User", back_populates="chats")
