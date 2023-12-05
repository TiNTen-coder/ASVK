import asyncio
from time import strftime

async def main():
    task3 = asyncio.create_task(late(3, 'three'))
    task4 = asyncio.create_task(late(4, 'four'))
    await(task3)
    print(f"> {strftime('%X')}")
    await(task4)
    print(f"> {strftime('%X')}")

async def late(delay, message):
    print(f'Start ({message})')
    asyncio.sleep(delay)
    print(message)
