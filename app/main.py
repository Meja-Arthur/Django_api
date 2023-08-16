import psycopg2 # pip3 install psycopg2
from psycopg2.extras import RealDictCursor
import time

from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Using pydantic to set the Schema of the data 
# in this schema if we put a string instead of an integer it will bring and error since it only
# allows integer for rating options 
class Post(BaseModel):
    # These is our schema and it returns an organised data 
    title: str
    content: str
    published: bool = True

   
 # connecting to my postgress data base using connections 
#  cursor_factory=RealDictCursor what this does is that it gives you the column name and it's values to 
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
            password='ima12546', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)




# using memory in storing our informations 
my_posts = [
    {"title": "This is the first", "content":"this is the body of the content", "id": 0},
    {"title": "The river of Babylon", "content":"the river that fed the israelites", "id":1}
    ]


# we want to retreive the information from the backend and update it back 
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
        
# Deleting function of a post 
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
        
        
# creating the post
# since this is a create function we should get a 201 status code for creation 
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": post}



# here we are retriving a single post the informations form the backend 
# Using HttPException is the best way for validation of our codes 
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    return {"post_details": post}
 

# Deleting a particular post in django 
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delele_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    my_posts.pop(index)
    return{"message": 'post was successfullt deleted'}


# Updating a post in the application programming interface
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict     
    return {"data": post_dict}
    



#getting all the posts from my database postgress 
@app.get("/posts")
def get_post():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}











@app.get("/")# all these 3 line of code is known as path operation
def root():
    return {"message": "Welcome to my Api server "}




#@app.post("/createpost/")
#def create_post(payload: dict = Body(...)):
#    print(payload)
    #return {"message": "Post created successfully."}
    # reffering to the created post 
    
    #return {"new_post": f"title {payload['title']} content {payload['content']}"}
    
# Using the Schema in the Post sent from the frontend 
# @app.post("/posts/")    
# def create_post(post: Post):
#     print(post)
#     # returning a dictionary version of the informations
#     print(post.dict())
#     return {"data": post}    