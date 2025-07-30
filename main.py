from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog,user,authentication
from fastapi.middleware.cors import CORSMiddleware



app =FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # or ["*"] for all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


