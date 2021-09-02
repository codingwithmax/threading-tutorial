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
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(30), 5), async_sleep(6), print_hello())
    except asyncio.TimeoutError:
        print('Encountered timeout error')
    print('total time:', time.time() - start)


if __name__ == "__main__":
    asyncio.run(main())
