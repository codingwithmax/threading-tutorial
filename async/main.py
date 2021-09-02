import asyncio
import time


async def async_sleep(n):
    print('Before sleep', n)
    await asyncio.sleep(n)
    print('After sleep', n)


async def print_hello():
    print('Hello')


async def main():
    start = time.time()
    await asyncio.gather(async_sleep(2), async_sleep(1), print_hello())
    print('total time:', time.time() - start)


if __name__ == "__main__":
    asyncio.run(main())
