def blog_schemas(blog) -> dict:
    return{
        "id": str(blog["_id"]),
        "author": blog["author"],
        "title": blog["title"],
        "content": blog["content"]
    }

def blogs_schemas(blogs) -> list:
    return [blog_schemas(blog) for blog in blogs ]