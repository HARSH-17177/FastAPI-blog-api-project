from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token,database,models
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(db: Session = Depends(database.get_db),data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # return token.verify_token(data, credentials_exception)
    # Verify token and extract user email
    token_data = token.verify_token(data, credentials_exception)
    if not token_data or not token_data.email:
        raise credentials_exception

    # Fetch the user from the database using the extracted email
    user = db.query(models.User).filter(models.User.email == token_data.email).first()
    if not user:
        raise credentials_exception

    return user