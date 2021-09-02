import asyncio
import time


async def async_sleep(n):
    print('Before sleep', n)
    n = max(2, n)
    for i in range(1, n):
        yield i
        await asyncio.sleep(i)
    print('After sleep', n)


async def print_hello():
    print('Hello')


async def main():
    start = time.time()
    async for k in async_sleep(5):
        print(k)
    print('total time:', time.time() - start)


if __name__ == "__main__":
    asyncio.run(main())
