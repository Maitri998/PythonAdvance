from fastapi import FastAPI

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id:int):
#     return {"item_id": item_id}

@app.get("/users/me")
async def read_users_me():
    return {"user_id":"the current user"}

@app.get("/users/{user_id}")
async def read_users(user_id):
    return {"user_id":user_id}

