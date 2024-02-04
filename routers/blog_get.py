from fastapi import APIRouter
from fastapi import status, Response, Depends
from enum import Enum
from typing import Optional
from .blog_post import required_functionality

router = APIRouter(prefix="/blog", tags=["blog"])

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


# If it is defined below `get_blog` I get an error message because 
# all functions defined below `get_blog` for which path starts from "blog" 
# must have follow rule "blog/integer" so order of functions is veeery important

# @app.get('/blog/all')
# def get_all_blogs():
#     return {"message": "All blogs provided"}

@router.get('/all', 
        #  tags=['blog'], 
         summary="Retrieve all blogs",
         description="This API call simulates fetching all blogs.",
         response_description="List of all blogs.")
def get_blogs(page: int=1, page_size: Optional[int] = None, req_parameters: dict=Depends(required_functionality)):
    return {"message": f"All {page_size} blogs on page {page}", "req": req_parameters}


@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool=True, username: Optional[str] = None):
    """Simulates retrieving a comment of blog 

    Args:

    - id (int): Path parameter
    - comment_id (int): Path parameter
    - valid (bool, optional): Query parameter. Defaults to True.
    - username (Optional[str], optional): Query parameter. Defaults to None.
    """
    return {"message": f"Blog_id: {id}, comment_id: {comment_id}, valid: {valid}, username: {username}"}

# defining fix available values: we do it using class that have specified
# class atributes
@router.get('/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type: {type}'}



@router.get('/{id}') # path parameter, can be used in a function
# Using type definition gives you sureness that only int will be recognized as valid type
# if I use for instance: http://127.0.0.1:8000/blog/3.3 I get an error message
def get_blog(id: int, response: Response): 
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}\
    
    response.status_code = status.HTTP_200_OK
    return {"message": f"Blog with ID: {id}"}