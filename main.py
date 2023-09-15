from fastapi import FastAPI
from enum import Enum
from routers import blog_get, blog_post

app = FastAPI() # instance od our application
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello') # attaching this function to endpoint
def hello_world():
    """Say Hello to:
        - you
        - me""" # will show up in documentation
    return {"message": "Hello World"}








# run app:  uvicorn main:app --reload
#                uvicorn <fine_name>:<instance_name> --reload