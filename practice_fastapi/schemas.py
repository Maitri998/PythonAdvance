from pydantic import BaseModel, EmailStr

#register user 
class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    password: str
#login user
class LoginUser(BaseModel):
    username: str
    password: str
#show all users present
class ShowUser(BaseModel):
    id: int
    username: str
    email: EmailStr
