from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title:str
    body:str
    
class Blog(BlogBase):
    class Config():
        orm_mode=True
       
class User(BaseModel):
    name:str
    email:str
    password:str
  
class ShowUser(BaseModel):
    name:str
    email:str
    blog:List[Blog]=[]
    class Config():
        # orm_mode=True 
        from_attributes =True        
        
class ShowBlog(BaseModel):
    # for only title,body return 
    title:str
    body:str
    
    creator:ShowUser
    class Config():
        # orm_mode=True
        from_attributes=True        