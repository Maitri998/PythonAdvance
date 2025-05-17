import bcrypt
from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET = "mysecretkey123"
ALGORITHM = "HS256"
TOKEN_EXPIRATION_MINUTES = 30

def hash_pass(password):
    # Turnpassword into hashed
    #covered in 17/05 referenced from https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_pass(plain_password, hashed_password):
    # Check password matches the hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_token(data: dict):
    # Make a copy of the data and add an expiration time
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    # Encode and return the JWT token
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token):
    # Try to decode the token and return the data inside
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
