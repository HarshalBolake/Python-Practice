import asyncio

# async def task(name, seconds):
#     print(f"{name} starting")
#     await asyncio.sleep(seconds)
#     print(f"{name} done")

# async def main():
#     await asyncio.gather(task("A",2),task("B",2))

# asyncio.run(main())


# async def greet():
#     return "Hello"

# async def main():
#     result = await greet()
#     print(result)

# asyncio.run(main())



# async def worker(name, delay):
#     print(f"{name}: start")
#     await asyncio.sleep(delay)
#     print(f"{name}: end")

# async def main():
#     await asyncio.gather(
#         worker("A",1),
#         worker("B",2),
#         worker("C",1)
#     )

# asyncio.run(main())


async def fetch(n):
    await asyncio.sleep(1)
    return n * n

# async def main():
#     reslts = await asyncio.gather(fetch(1),fetch(2),fetch(3))
#     print(reslts)

# asyncio.run(main())


async def main():
    task = asyncio.create_task(fetch(5))
    print("doing other work while fetch runs.....")
    result = await task
    print(result)

asyncio.run(main())