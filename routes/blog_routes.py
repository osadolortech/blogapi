import fastapi


from fastapi import APIRouter
from config.database import collection_post
from models.blog_models import Blog
from schemas.blog_shema import blog_schemas,blogs_schemas
from bson import ObjectId

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

@blog_route.get("/{id}")
async def get_single_post(id: str):
    blog = blogs_schemas(collection_post.find({"_id": ObjectId(id)}))
    return {"status":"ok", "get_single_post": blog}

@blog_route.put("/{id}")
async def update_post(id: str, blog: Blog):
    collection_post.find_one_and_update({"_id": ObjectId(id)},{
        "$set": dict(blog)
    })
    blog = blogs_schemas(collection_post.find({"_id":ObjectId(id)}))
    return{"status": "ok", "update":blog}

@blog_route.delete("/{id}")
async def delete_post(id: str):
    collection_post.find_one_and_delete({"_id": ObjectId(id)})
    return{"status":"ok", "deleted":"post has been deleted"}
