from fastapi import APIRouter, Query, Path
from models.user import User
from db.connection import db

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: str = Path(..., title="The ID of the user to retrieve")):
    user = db.users.find_one({"id": user_id})
    return user

@router.post("/create_user/")
async def create_user(user: User):
    db.users.insert_one(user.dict())
    return {"message": "User created successfully"}

@router.put("/update_user/{user_id}")
async def update_user(user_id: str, user: User):
    db.users.update_one({"id": user_id}, {"$set": user.dict()})
    return {"message": "User updated successfully"}

@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: str):
    db.users.delete_one({"id": user_id})
    return {"message": "User deleted successfully"}

@router.get("/users/list_users")
async def list_users(name: str = Query(None, title="Filter users by name")):
    query = {}
    if name:
        query["name"] = name
    users = db.users.find(query, {"_id": 0})
    return list(users)
