import asyncio
import time


async def async_sleep():
    print('in async sleep, at time', time.time())
    await asyncio.sleep(5)
    print('Finished sleeping')


async def print_hello():
    print('in print hello, at time', time.time())
    print('Hello')


async def main():

    start = time.time()
    await asyncio.gather(async_sleep(), print_hello(), async_sleep())
    print('Finished gather, took', time.time() - start)

asyncio.run(main())