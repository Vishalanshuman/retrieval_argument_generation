from fastapi import APIRouter, Depends, HTTPException, UploadFile, File,status
from sqlalchemy.orm import Session
from config import schemas
from config.database import get_db
from config import models
from config.oauth import get_hashed_password,validate_password,create_jwt_token,get_current_user
import os
import shutil

router = APIRouter(prefix="/auth", tags=["Authentication"])

IMAGE_UPLOAD_DIR = "static/images"

if not os.path.exists(IMAGE_UPLOAD_DIR):
    os.makedirs(IMAGE_UPLOAD_DIR)

@router.post("/signup", response_model=schemas.UserOutput)
async def signup(user:schemas.UserCreate ,db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password=get_hashed_password(user.password)
    new_user = models.User(
        email=user.email,
        hashed_password=user.password,
        is_admin=user.is_admin
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login",response_model=schemas.Token)
def login(creds:schemas.Login,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==creds.email).first()
    if not user or not validate_password(password=creds.password,hashed_password=user.hashed_password):
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials.")
    jwt_token = create_jwt_token({"sub":str(user.id)})
    return jwt_token

