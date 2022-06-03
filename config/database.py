from http import client
from os import getenv
from pymongo import MongoClient

URL = getenv("URL")

client = MongoClient(URL)

db = client.blog_application

collection_post = db["blog_api"]
collection_comment = db["comment_api"]