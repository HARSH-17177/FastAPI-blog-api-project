from typing import List
from fastapi import APIRouter,Depends,status

from blog import models
from .. import schemas,database,oauth2
from sqlalchemy.orm import Session
from ..repository import blog_repo

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db=database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def get_all_blog(db: Session=Depends(get_db)):
    return blog_repo.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog,db: Session=Depends(get_db),current_user:models.User = Depends(oauth2.get_current_user)):
    return blog_repo.create(request,db,current_user)


@router.get('/{input}',status_code=200,response_model=List[schemas.ShowBlog])
def get_blogby_string(input,db: Session=Depends(get_db)):
    return blog_repo.get_by_string(input,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id,db:Session=Depends(get_db)):
    return blog_repo.delete_by_id(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog_by__id(id,request:schemas.Blog,db:Session=Depends(get_db)):
    return blog_repo.update_by_id(id,request,db)