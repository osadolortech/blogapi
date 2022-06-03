import fastapi


from fastapi import APIRouter
from config.database import collection_post
from models.blog_models import Blog
from schemas.blog_shema import blog_schemas,blogs_schemas

blog_route = APIRouter()

@blog_route.get("/")
async def get_all_post():
    blog = blogs_schemas(collection_post.find())
    return {"status": "ok", "All_post": blog}

@blog_route.post("/")
async def blog_post(blog: Blog):
    _id = collection_post.insert_one(dict(blog))
    blog = blogs_schemas(collection_post.find({"_id": _id.inserted_id}))
    return {"status": "ok", "post_blog": blog}
    
