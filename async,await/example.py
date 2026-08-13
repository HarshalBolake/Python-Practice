import asyncio
import aiohttp

async def fetch_user(session,username):
    async with session.get(f"https://api.github.com/users/{username}")as resp:
        data = await resp.json()
        return data["name"]

async def main():
    usernames = ["octocat", "torvalds", "gvanrossum"]
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch_user(session, u) for u in usernames])
        print(results)

asyncio.run(main())