from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models,hashing,token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with Username : {request.username} not found")
    if not hashing.Hash().verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    
    # generate a jwt token and return
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

    