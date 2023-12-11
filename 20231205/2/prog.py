import asyncio
import random


async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()
    first_pointer, second_pointer, third_pointer = start, middle, start
    while first_pointer < middle or second_pointer < finish:
        if second_pointer == finish or (first_pointer < middle and A[first_pointer] < A[second_pointer]):
            B[third_pointer] = A[first_pointer]
            first_pointer += 1
        else:
            B[third_pointer] = A[second_pointer]
            second_pointer += 1
        third_pointer += 1
    event_out.set()


async def mtasks(A):
    A_copied = A.copy()
    tasks = []
    events = []
    for i in range(len(A)):
        events.append(asyncio.Event())
        events[i].set()
    indexer = 1
    counter = 1
    length = len(A)
    B = [0] * length
    event_indexer = 0
    while indexer < length:
        first_array = B
        second_array = A_copied
        if counter & 1:
            first_array = A_copied
            second_array = B
        for j in range(0, length, indexer * 2):
            start = j
            middle = length - 1
            finish = length
            if middle > indexer + j:
                middle = indexer + j
            if finish > 2 * indexer + j:
                finish = 2 * indexer + j
            new_event = asyncio.Event()
            tasks.append(asyncio.create_task(
                merge(first_array, second_array, start, middle, finish, *events[event_indexer:event_indexer + 2],
                      new_event)))
            events += [new_event]
            event_indexer += 2
        events.append(new_event)
        counter = 1 - counter
        indexer *= 2
    ans = (tasks, B)
    if counter & 1:
        ans = (tasks, A_copied)
    return ans


import sys
exec(sys.stdin.read())
