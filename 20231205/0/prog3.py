import asyncio
from time import strftime

async def main():
    res = await asyncio.gather(
        late(3, 'three'),
        late(1, 'one'),
        late(2, 'two')
    )
    print(res)

async def late(delay, message):
    print(f'Start ({message})')
    await asyncio.sleep(delay)
    print(message)
    return delay

asyncio.run(main())
