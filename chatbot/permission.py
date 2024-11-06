from config.oauth import get_current_user
from config.models import User
from fastapi import Depends,HTTPException,status

def verify_admin_user(current_user: User = Depends(get_current_user)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Need Admin credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    if not current_user.is_admin:
        raise credentials_exception
    
    return current_user
