import asyncio
import time

async def fetch_data(id,delay):
    print("veri alınıyor... id:",id)
    await asyncio.sleep(delay)
    print("veri alındı... id:",id)
    return {"id":id,"data":"bazı veriler"}

async def main():
    task1 = asyncio.create_task(fetch_data(1,2))
    task2 = asyncio.create_task(fetch_data(2,3))
    task3 = asyncio.create_task(fetch_data(3,1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(f"Alınan veri: {result1}")
    print(f"Alınan veri: {result2}")
    print(f"Alınan veri: {result3}")

#  bu sistemle delay suresı en uzun olanın resultı dönesiye kadar diğerlerininki dönmüş olur 
t = time.time()
asyncio.run(main())
print(time.time()-t)