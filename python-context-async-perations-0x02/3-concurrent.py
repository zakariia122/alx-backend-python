import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect("my_database.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users
        
async def async_fetch_older_users():
    async with aiosqlite.connect("my_database.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            return older_users

async def fetch_concurrently():
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("🔹 All Users:", all_users)
    print("🔸 Older Than 40:", older_users)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
