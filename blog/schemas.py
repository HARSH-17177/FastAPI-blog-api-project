from pydantic import BaseModel
from typing import List,Optional


# pydantic models are called schemas while 
# sqlachamey models are called models
#This class directly inherits from Pydantic’s BaseModel. It defines the basic schema for a blog with two fields: title and body. This is a plain Pydantic model used for data validation and serialization.
class Blog(BaseModel):
    title:str
    body: str

# This class inherits from your own Blog class, so it gets all the fields (title and body) from Blog. The only addition is the inner Config class with from_attributes=True, which allows Pydantic to create models from ORM objects (like SQLAlchemy models) using their attributes.    
class BlogBase(Blog):
    class Config():
        from_attributes=True    


class User(BaseModel):
    name:str
    email:str
    password:str


# this is the model(schema) which we are using as response to show as alchamy model also return id
class ShowUser(BaseModel):
    name:str
    email:str  
    blogs: List[BlogBase]=[]
    class Config():
        from_attributes=True   

class ShowUser_without_its_blog(BaseModel):
    name:str
    email:str 



class ShowBlog(BaseModel):
    title:str
    body: str    
    creator: ShowUser_without_its_blog
    class Config():
        from_attributes=True   


class Login(BaseModel):
    username:str
    password:str          


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None           
