#this get a single post 
def blog_schemas(blog) -> dict:
    return{
        "id": str(blog["_id"]),
        "author": blog["author"],
        "title": blog["title"],
        "content": blog["content"]
    }

# this gets all the blog post
def blogs_schemas(blogs) -> list:
    return [blog_schemas(blog) for blog in blogs ]