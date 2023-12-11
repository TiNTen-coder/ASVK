import asyncio

event = asyncio.Event()


async def writer(queue, delay):
    indexer = 0
    while True:
        await asyncio.sleep(delay)
        await queue.put(f'{indexer}_{delay}')
        if event.is_set():
            break
        indexer += 1


async def stacker(queue, stack):
    while True:
        await asyncio.sleep(0)
        ans = await queue.get()
        await stack.put(ans)
        if event.is_set():
            break


async def reader(stack, counter, delay):
    while counter:
        await asyncio.sleep(delay)
        while not stack:
            await asyncio.sleep(0)
        ans = await stack.get()
        print(ans)
        counter -= 1
    event.set()


async def main():
    queue = asyncio.Queue()
    stack = asyncio.LifoQueue()
    delay1, delay2, delay3, count = eval(input())
    await asyncio.gather(
        writer(queue, delay1),
        writer(queue, delay2),
        stacker(queue, stack),
        reader(stack, count, delay3)
    )


asyncio.run(main())

