import fastapi
from fastapi import APIRouter
from config.database import collection_post,collection_comment
from models.blog_models import Blog,Comment,ObjectIdStr
from schemas.blog_shema import blog_schemas,blogs_schemas,comment_schema,comments_schema
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
async def get_single_post(id: str, comment: Comment):
    comment = comments_schema(collection_comment.find())
    blog = blogs_schemas(collection_post.find({"_id": comment.ObjectId(id)}))
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


# @blog_route.get("/comment/all_coment/{post}")
# async def get_comment():
#     comment = comments_schema(collection_comment.find())
#     return {"status":"ok", "get_all_comments": comment}

@blog_route.post("/comment")
async def post_comment(comment: Comment):
    _id = collection_comment.insert_one(dict(comment))
    comment = comments_schema(collection_comment.find({"_id": _id.inserted_id}))
    return {"status":"ok", "post_comment": comment}

@blog_route.get("/comment/{id}")
async def single_comment(id: ObjectIdStr):
    comment = comments_schema(collection_comment.find({"_id": ObjectId(id)}))
    return {"status":"ok", "get_all_comments": comment}

@blog_route.get("/comment/all_coment/{post}")
async def all_comment(post: ObjectIdStr):
    comment = comments_schema(collection_comment.find({"post": post}))
    return {"status":"ok", "get_all_comments": comment}

