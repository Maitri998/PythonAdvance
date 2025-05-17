from fastapi import FastAPI, Depends, HTTPException
from database import create_table
import schemas, models
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Security
from utils import verify_pass, create_token
from auth import get_logged_in_user

app = FastAPI()

# Create users table when app starts
create_table()

@app.post("/register")
def register(user: schemas.RegisterUser):
    
    #Register a new user with username, email, and password.
    models.add_user(user)
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: schemas.LoginUser):

   # Login user with username and password.
    #Returns JWT token if credentials are correct.

    db_user = models.find_user_by_username(user.username)
    if not db_user:
        raise HTTPException(status_code=401, detail="Wrong username or password")
    if not verify_pass(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Wrong username or password")
    token = create_token({"sub": db_user["username"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/users", response_model=list[schemas.ShowUser])
def read_users(current_user=Depends(get_logged_in_user)):
#    List all users.
 #   Requires user to be logged in with a valid token.
  
    return models.get_all_users()

@app.delete("/users/{user_id}")
def delete_user(user_id: int, current_user=Depends(get_logged_in_user)):

    #Delete a user by their id.
    #Requires authentication.
 
    models.remove_user(user_id)
    return {"message": "User deleted"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: schemas.RegisterUser, current_user=Depends(get_logged_in_user)):
    
    #Update a user's information.
    #Can update username, email, and password.
    models.change_user(user_id, user)
    return {"message": "User updated"}
