from pydantic import BaseModel
from bson.objectid import  ObjectId

from bson.errors import InvalidId

class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        try:
            ObjectId(v)
        except InvalidId:
            raise ValueError("Not a VALID OBJECTID")
        return str(v)


class Blog(BaseModel):
    author: str
    title: str
    content: str


class Comment(BaseModel):
    content: str  
    post: ObjectIdStr


