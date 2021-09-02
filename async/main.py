import asyncio
import time


<<<<<<< Updated upstream
async def async_sleep():
    print('in async sleep, at time', time.time())
    await asyncio.sleep(5)
    print('Finished sleeping')
=======
async def async_sleep(n):
    print('Before sleep', n)
    n = max(2, n)
    for i in range(1, n):
        yield i
        await asyncio.sleep(i)
    print('After sleep', n)
>>>>>>> Stashed changes


async def print_hello():
    print('in print hello, at time', time.time())
    print('Hello')


async def main():

    start = time.time()
<<<<<<< Updated upstream
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(), 1),
                             print_hello(),
                             async_sleep())
    except asyncio.TimeoutError:
        print('Encountered timeout error')
    print('Finished gather, took', time.time() - start)
=======
    async for k in async_sleep(5):
        print(k)
    print('total time:', time.time() - start)

>>>>>>> Stashed changes

asyncio.run(main())