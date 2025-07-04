import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger


app = FastAPI()


class User(BaseModel):
    user_id: int
    name: str
    email: str


# Mock database
users_db = []


@app.get("/users")
async def get_users():
    return users_db


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # if 0 <= user_id < len(users_db):
    for user in users_db:
        if user.get("user_id") == user_id:
            logger.info(f"Nice nashel id {user_id}")
            return user
    return {"error": "User not found"}


@app.post("/users")
async def create_user(user: User):
    users_db.append(user.dict())
    return {"id": len(users_db) - 1, **user.dict()}


@app.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    for user in users_db:
        logger.info(user)
        if user.get("user_id") == user_id:
            logger.info(f"Nice nashel id {user_id}")
            users_db.remove(user)
    return {"error": "User not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
