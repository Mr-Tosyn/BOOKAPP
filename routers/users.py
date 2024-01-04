from fastapi import APIRouter
from schemas.user_schema import User 

users_router = APIRouter()

Users = [
    User(username="johndoe", age=25),
    User(username="Adewale", age=70)
]

@users_router.get("/")
def get_users():
    return users    
 