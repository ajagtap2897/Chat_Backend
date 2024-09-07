from datetime import datetime
import json
from pathlib import Path
import uuid
from fastapi import FastAPI, HTTPException, status, Depends
from typing import List
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from models.user_model import User
from uuid import UUID, uuid4
from models.message_model import CreateMessageRequest, Message
from fastapi.middleware.cors import CORSMiddleware

MONGO_URI = "mongodb+srv://ajagtap1307:wZX2E3zKy9blwZJ1@cluster0.opkxh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(MONGO_URI)
db = client.chatty_chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.). Restrict in production if necessary
    allow_headers=["*"],  # Allows all headers. Restrict in production if necessary
)

static_path = Path(__file__).resolve().parent / "static"

# Mount the static files directory
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Dependency to get MongoDB collections
def get_user_collection():
    return db.user

def get_message_collection():
    return db.message


@app.get("/chat-list/{user_id}")
async def getChatList(user_id: str, messages=Depends(get_message_collection), users = Depends(get_user_collection)):
    messageList = await messages.find({'$or': [{ "sender": user_id },{ "receiver": user_id }]}).to_list(None)
    
    related_ids = set()
    for message in messageList:
        if message['sender'] == user_id:
            related_ids.add(message['receiver'])
        elif message['receiver'] == user_id:
            related_ids.add(message['sender'])

    related_users = await users.find({'_id': {'$in': list(related_ids)}}).to_list(None)
    
    result = []
    for related_user in related_users:
        last_message = await messages.find({'$or': [{ 'sender': user_id, 'receiver': related_user['_id'] },{ 'sender': related_user['_id'], 'receiver': user_id }]}).sort('timestamp', -1).limit(1).to_list(None)
        
        result.append({
            'user': related_user,
            'last_message': last_message[0]
        })
    
    return result


@app.get("/chat-history/{user_id}/{contact_id}")
async def getChatList(user_id: str, contact_id: str, messages=Depends(get_message_collection), users = Depends(get_user_collection)):
    messageList = await messages.find({'$or': [{ 'sender': user_id, 'receiver': contact_id },{ 'sender': contact_id, 'receiver': user_id }]}).sort('timestamp', -1).to_list(None)

    contactUser = await users.find({'_id': contact_id}).to_list(None)

    return {
        "contactUser": contactUser[0],
        "messageList": messageList
    }

# CRUD for Messages
@app.post("/messages", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_message(message: CreateMessageRequest, messages=Depends(get_message_collection)):
    newMessage = {
        "_id": str(uuid.uuid4()),  # Set the custom UUID as the _id
        "content": message.content,
        "created_at": str(datetime.now()),
        "sender": message.sender,
        "receiver": message.receiver,
    }
    
    result = await db.message.insert_one(newMessage)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")

    return newMessage

@app.get("/users/{user_id}")
async def get_user(user_id: str, users=Depends(get_user_collection)):
    user = await users.find({'_id': user_id}).to_list(None)
    return user[0]




# CRUD for Users
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User, users=Depends(get_user_collection)):
    if await users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    await users.insert_one(user.dict())
    return user

@app.get("/users/", response_model=List[User])
async def get_users(users=Depends(get_user_collection)):
    return await users.find().to_list(None)



@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: UUID, user: User, users=Depends(get_user_collection)):
    updated_user = await users.find_one_and_update(
        {"id": user_id}, {"$set": user.dict()}, return_document=True
    )
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: UUID, users=Depends(get_user_collection)):
    result = await users.delete_one({"id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return None



@app.get("/messages/", response_model=List[Message])
async def get_messages(messages=Depends(get_message_collection)):
    return await messages.find().to_list(length=100)

@app.get("/messages/{message_id}", response_model=Message)
async def get_message(message_id: UUID, messages=Depends(get_message_collection)):
    message = await messages.find_one({"id": message_id})
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

@app.put("/messages/{message_id}", response_model=Message)
async def update_message(message_id: UUID, message: Message, messages=Depends(get_message_collection)):
    updated_message = await messages.find_one_and_update(
        {"id": message_id}, {"$set": message.dict()}, return_document=True
    )
    if updated_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return updated_message

@app.delete("/messages/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_message(message_id: UUID, messages=Depends(get_message_collection)):
    result = await messages.delete_one({"id": message_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Message not found")
    return None