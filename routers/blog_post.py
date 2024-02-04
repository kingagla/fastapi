from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix = '/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key1": "val1"}
    image: Image = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int=1):
    return {
        "id": id,
        "data": blog,
        "version": version
        }

@router.post('/new/{id}/comment/{comment_id}')
def  create_comment(blog: BlogModel, 
                    id: int, 
                    comment_title: int = Query(None,
                                            title="Id of the comment",
                                            description="Some description for comment_title",
                                            alias="commentTitle", 
                                            depricated=True),
                    content: str = Body(Ellipsis,# ... albo default "aaa"
                                        min_length=10, # minimalna długość 
                                        max_length=50, # maksymalna długość
                                        regex="^[a-z\s]*$"),
                    v: List[str] = Query(['a', 'b', 'c']),
                    comment_id: int = Path(qe=5, le=10)
                    ):
    return {
        'blog': blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id,
    }
    
def required_functionality():
    return {"message": "Learning fastAPI is important."}