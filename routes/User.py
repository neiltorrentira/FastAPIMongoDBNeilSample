from fastapi import APIRouter, HTTPException
from models.User import User
from config.database import connectDB
from schemas.User import serializeDict, serializeList, userEntity
from bson import ObjectId

# 'user' is the database name @local database
user = APIRouter()


# Get/Query All User
@user.get('/')
async def find_All_Users():
    print(serializeList(connectDB.local.user.find()))
    return serializeList(connectDB.local.user.find())


# Get/Query User by ID
@user.get('/{id}')
async def find_One_User(id: str):
    print(serializeDict(connectDB.local.user.find_one({"_id": ObjectId(id)})))
    # No Error handling if 'ID' doesn't exist
    # if id not in connectDB.local.user.find_one({"_id": ObjectId(id)}):
    #     raise HTTPException(status_code=404, detail="Item not found")
    return serializeDict(connectDB.local.user.find_one({"_id": ObjectId(id)}))


# Create User
@user.post('/')
async def create_User(user: User):
    connectDB.local.user.insert_one(dict(user))
    print(serializeList(connectDB.local.user.find()))
    return serializeList(connectDB.local.user.find())


# Update User
@user.put('/{id}')
async def update_User(id, user: User):
    connectDB.local.user.find_one_and_update({"_id": ObjectId(id)},
                                             {"$set": dict(user)})
    print(serializeDict(connectDB.local.user.find_one({"_id": ObjectId(id)})))
    return serializeDict(connectDB.local.user.find_one({"_id": ObjectId(id)}))


# Delete User
@user.delete('/{id}')
async def delete_User(id):
    # When using 'serializeDict' for delete, 500 Internal Server Error occurs
    # Using 'userEntity' instead
    # No Error handling if 'ID' doesn't exist
    # return(serializeDict(connectDB.local.user.find_one_and_delete({"_id":ObjectId(id)})))
    return userEntity(connectDB.local.user.find_one_and_delete({"_id": ObjectId(id)}))
