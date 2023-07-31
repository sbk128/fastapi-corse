from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from pydantic import BaseSettings
from .routers import post, user, auth, vote
from .config import settings

class Settings(BaseSettings):
    database_password : str = "localhost"
    database_username: str = "postgres"
    secret_key: str = "fahyb56yn46y4ny6yettny"

settings = Settings()

# This command is used to create the tables using sqlalchemy for alembic it is not needed
# models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# my_posts = [{"title": "title post 1", "content": "content post 1", "id": 1},
#             {"title": "Fav food", "content": "PAASTTAAA", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#             if p['id'] == id:
#                 return i 

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router) 

@app.get("/")
async def root():
    return {"message": "Hello World"}



# title: str, content: str, category: boolean
 
# https://youtu.be/0sOvCWFmrtA?t=37943

# uvicorn app.main:app --reload