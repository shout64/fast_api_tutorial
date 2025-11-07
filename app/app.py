from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "This is my new cool post"},
    2: {
        "title": "Another Day, Another Post",
        "content": "Just sharing some thoughts today.",
    },
    3: {
        "title": "Tech Talk",
        "content": "Exploring the latest in AI and machine learning.",
    },
    4: {
        "title": "Foodie Adventures",
        "content": "My review of the new downtown cafe.",
    },
    5: {
        "title": "Travel Diaries",
        "content": "Recap of my trip to the mountains.",
    },
    6: {
        "title": "Learning Python",
        "content": "Tips and tricks for getting started with FastAPI.",
    },
    7: {
        "title": "Random Musings",
        "content": "Just some scattered thoughts on life and everything.",
    },
    8: {
        "title": "Book Review: The Great Gatsby",
        "content": "A timeless classic that still resonates today.",
    },
    9: {
        "title": "Fitness Journey",
        "content": "Sharing my progress and challenges in staying active.",
    },
    10: {
        "title": "Weekend Vibes",
        "content": "What I'm looking forward to this Saturday and Sunday.",
    },
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return list(text_posts.values())

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
