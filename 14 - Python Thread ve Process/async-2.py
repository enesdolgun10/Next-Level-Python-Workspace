import asyncio

async def fetch_data(delay):
    print("veri alınıyor")
    await asyncio.sleep(delay)
    print("veri alındı...")
    return {"data":"bazı veriler"}

async def main():
    print("start")
    
    # task = fetch_data(2)
    # result = await task

    result = await fetch_data(2)

    print(f"Alınan veri : {result}")
    print("end")


asyncio.run(main())