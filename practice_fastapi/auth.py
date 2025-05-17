from fastapi import Security, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from utils import decode_token

bearer_scheme = HTTPBearer()
#refrenced from https://auth0.com/blog/how-to-handle-jwt-in-python/
def get_logged_in_user(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    token = credentials.credentials  # Extracts the token part only
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token invalid or expired")
    return payload
