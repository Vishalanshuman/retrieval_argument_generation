from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class Token(BaseModel):
    access_token : str
    token_type :str

class LoginForm(BaseModel):
    email:EmailStr
    password:str

class Login(BaseModel):
    email : str
    password :str

class UserCreate(BaseModel):
    email:str
    password:str
    is_admin:bool=False


class UserOutput(BaseModel):
    id:int
    email:EmailStr
    hashed_password:str
    created_at:datetime

class DocumentRecordOut(BaseModel):
    id:int
    filename:str
    file_path:str
    uploaded_at:datetime
    user_id:int

class Question(BaseModel):
    question:str
class Answer(Question):
    answer:str
