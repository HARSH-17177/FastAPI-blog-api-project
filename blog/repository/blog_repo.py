from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Depends
from .. import models,schemas,oauth2


def get_all(db:Session):
    blog = db.query(models.Blog).all()
    return blog 

def create(request: schemas.Blog, db: Session, current_user: models.User = Depends(oauth2.get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

def get_by_string(input: str, db: Session):
    keyword = f"%{input}%"
    filterd_blog = db.query(models.Blog).join(models.User).filter(
        (models.Blog.title.ilike(keyword)) |
        (models.Blog.body.ilike(keyword)) |
        (models.User.name.ilike(keyword)) |
        (models.User.email.ilike(keyword))
    ).all()
    if not filterd_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with input {input} not found"
        )
    return filterd_blog

def delete_by_id(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'

def update_by_id(id:int,request:schemas.Blog,db:Session):
    blog =db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.update({
        models.Blog.title: request.title,
        models.Blog.body: request.body
    })
    db.commit()
    return 'Updated'
