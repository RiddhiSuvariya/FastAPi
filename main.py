from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
def index(limit,published: bool,sort:Optional[str]=None):
    # return published
    if published:
        return {'data': f'{limit} published blog from database'}
    else:
        return {'data': f'{limit} blog from database'}

@app.get("/blog/unpublished")
def unpublished():
     return {'data':'all unpublished blogs'}
    
   
@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id =id
    return {'data': id}

 
    
@app.get('/blog/{id}/comments')
def comments(id):
    # return limit
    return {'data':{'1','2'}}


class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]    
    
    
@app.post('/blog')
def create_blog(blog:Blog):
    # return request
    return {'data':f'Blog is created with title {blog.title}'}