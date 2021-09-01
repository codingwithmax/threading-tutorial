import asyncio
import time


async def async_sleep():
    await asyncio.sleep(5)
    print('Finished sleeping')


async def return_hello():
    print('Hello')


async def main():
    task = asyncio.create_task(async_sleep())
    start = time.time()
    await asyncio.sleep(5)
    print('Finished sleeping for 5 seconds, took', time.time() - start)
    await task
    print('Finished awaiting task, took', time.time() - start)
    await return_hello()
    print('Finished printing hello, took', time.time() - start)

asyncio.run(main())