from http import client
from pymongo import MongoClient

client = MongoClient("mongodb+srv://FinalBlog :Computer333@cluster0.ve2nnja.mongodb.net/mainblog?retryWrites=true&w=majority")

db = client.blog_application

collection_post = db["blog_api"]