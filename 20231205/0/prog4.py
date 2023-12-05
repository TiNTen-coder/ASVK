import asyncio

async def squarer(x):
    return x ** 2

async def doubler(x):
    return 2 * x

async def main(*args):
    res = await asyncio.gather(*(squarer(i) for i in args))
    res = await asyncio.gather(*(doubler(i) for i in res))
    print(*res)

asyncio.run(main(*map(int, input().split())))
