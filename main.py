from db import models
from db.database import engine
from fastapi import FastAPI
from routers import article, blog_get, blog_post, users

app = FastAPI()  # instance od our application
app.include_router(users.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")  # attaching this function to endpoint
def hello_world():
    """Say Hello to:
    - you
    - me"""  # will show up in documentation
    return {"message": "Hello World"}


models.Base.metadata.create_all(engine)


# uvicorn app:  uvicorn main:app --reload
#                uvicorn <fine_name>:<instance_name> --reload


# TODO: coś nie dziala! Naprawić i stara baza jest pod nazwa v1
