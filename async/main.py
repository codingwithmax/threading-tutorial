import asyncio


async def async_sleep():
    await asyncio.sleep(5)
    print('Finished sleeping')


async def return_hello():
    return 'Hello'


async def main():
    await async_sleep()
    hello = await return_hello()
    print(hello)

asyncio.run(main())