from http import client
from os import getenv
from pymongo import MongoClient

username = getenv("DB_USERNAME")
password = getenv("DB_BASE")

client = MongoClient("mongodb+srv://username:password@cluster0.ve2nnja.mongodb.net/mainblog?retryWrites=true&w=majority")

db = client.blog_application

collection_post = db["blog_api"]