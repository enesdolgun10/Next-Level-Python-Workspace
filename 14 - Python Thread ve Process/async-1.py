import asyncio

async def main(msg):
    print("start")
    await asyncio.sleep(2)
    print(msg)

# c_obj = main("merhaba")
# asyncio.run(c_obj)

asyncio.run(main("merhaba"))