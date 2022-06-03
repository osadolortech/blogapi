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