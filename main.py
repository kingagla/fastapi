from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI() # instance od our application

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/hello') # attaching this function to endpoint
def hello_world():
    """Say Hello to:
        - you
        - me""" # will show up in documentation
    return {"message": "Hello World"}


# If it is defined below `get_blog` I get an error message because 
# all functions defined below `get_blog` for which path starts from "blog" 
# must have follow rule "blog/integer" so order of functions is veeery important

# @app.get('/blog/all')
# def get_all_blogs():
#     return {"message": "All blogs provided"}

@app.get('/blog/all')
def get_all_blogs(page: int=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool=True, username: Optional[str] = None):
    return {"message": f"Blog_id: {id}, comment_id: {comment_id}, valid: {valid}, username: {username}"}

# defining fix available values: we do it using class that have specified
# class atributes
@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type: {type}'}



@app.get('/blog/{id}') # path parameter, can be used in a function
# Using type definition gives you sureness that only int will be recognized as valid type
# if I use for instance: http://127.0.0.1:8000/blog/3.3 I get an error message
def get_blog(id: int): 
    return {"message": f"Blog with ID: {id}"}



# run app:  uvicorn main:app --reload
#                uvicorn <fine_name>:<instance_name> --reload