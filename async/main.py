import asyncio
import time


async def async_sleep(n):
    print('Before sleep', n)
    await asyncio.sleep(5)
    print('After sleep', n)


async def print_hello():
    print('Hello')


async def main():
    start = time.time()
    task = asyncio.create_task(async_sleep(1))
    await async_sleep(2)
    await print_hello()
    await task
    print('total time:', time.time() - start)


if __name__ == "__main__":
    asyncio.run(main())
