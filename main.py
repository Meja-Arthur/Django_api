from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")# all these 3 line of code is known as path operation
def root():
    return {"message": "Welcome to my Api server "}

@app.get("/post/")
def get_post():
    return {"post": "This is your Post"}


@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "Post created successfully."}