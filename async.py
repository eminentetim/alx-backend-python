import asyncio

async def greet(name):
    print(f"Hello {name}")
    await asyncio.sleep(10)
    print(f"stay {name}")
    await asyncio.sleep(10)
    print(f"Goodbye {name}")

asyncio.run(greet("Emmy"))

