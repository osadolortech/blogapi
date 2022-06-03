from pydantic import BaseModel


class Blog(BaseModel):
    author: str
    title: str
    content: str

class Comment(BaseModel):
    content: str  