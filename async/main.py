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
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(), 1),
                             print_hello(),
                             async_sleep())
    except asyncio.TimeoutError:
        print('Encountered timeout error')
    print('Finished gather, took', time.time() - start)

asyncio.run(main())