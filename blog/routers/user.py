from fastapi import APIRouter,Depends,status
from .. import database,schemas
from sqlalchemy.orm import Session
from ..repository import user_repo

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db



@router.post('/',response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user_repo.create(request,db)


@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user_repo.get_by_id(id,db)
