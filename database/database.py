#(©)CodeXBotz




import pymongo, os
from config import DB_URI, DB_NAME




from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(DB_URI)
db = client['telegram_bot']

async def add_user(user_id):
    await db.users.update_one({"id": user_id}, {"$set": {"id": user_id}}, upsert=True)

async def del_user(user_id):
    await db.users.delete_one({"id": user_id})

async def full_userbase():
    users = await db.users.find().to_list(None)
    return [user['id'] for user in users]

async def present_user(user_id):
    user = await db.users.find_one({"id": user_id})
    return user is not None

async def add_admin(admin_id):
    await db.admins.update_one({"id": admin_id}, {"$set": {"id": admin_id}}, upsert=True)

async def remove_admin(admin_id):
    await db.admins.delete_one({"id": admin_id})

async def is_admin(user_id):
    admin = await db.admins.find_one({"id": user_id})
    return admin is not None

async def update_forcesub(channel):
    await db.config.update_one({"key": "FORCE_SUB_CHANNEL"}, {"$set": {"value": channel}}, upsert=True)

async def get_forcesub():
    config = await db.config.find_one({"key": "FORCE_SUB_CHANNEL"})
    return config["value"] if config else None
