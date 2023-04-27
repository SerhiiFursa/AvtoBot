import os

import asyncpg
from dotenv import load_dotenv


async def connect_to_database():
    load_dotenv()
    conn = await asyncpg.connect(
            user=str(os.getenv("user_db")),
            password=str(os.getenv("password_db")),
            database=str(os.getenv("database")),
            port=str(os.getenv("port")),
            host=str(os.getenv("host"))
        )
    return conn
