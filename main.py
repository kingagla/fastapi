from db import models
from db.database import engine
from exceptions import StoryException
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
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


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418, content={"detail": exc.name}  # I am not a teapot XD
    )


# @app.exception_handler(HTTPException)
# def custom_exception_handler(request: Request, exc: HTTPException):
#     return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)


# uvicorn app:  uvicorn main:app --reload
#                uvicorn <fine_name>:<instance_name> --reload


# TODO: coś nie dziala! Naprawić i stara baza jest pod nazwa v1
