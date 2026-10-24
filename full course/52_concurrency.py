"""Concurrency allows tasks to make progress using threads, processes, or async operations.
This example shows a small task with each approach; each has different use cases and tradeoffs.
"""

# Topic 52: Threads, processes, and async/await

import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def square(number):
    return number * number


async def async_greeting(name):
    await asyncio.sleep(0)
    return f"Hello, {name}!"


async def main():
    numbers = [1, 2, 3, 4]

    # Threads are useful for work that waits on input/output.
    with ThreadPoolExecutor(max_workers=2) as executor:
        thread_results = list(executor.map(square, numbers))
    print("Thread results:", thread_results)

    # Processes can run CPU work in separate Python processes.
    with ProcessPoolExecutor(max_workers=2) as executor:
        process_results = list(executor.map(square, numbers))
    print("Process results:", process_results)

    # asyncio runs cooperative asynchronous tasks.
    print(await async_greeting("Maya"))


if __name__ == "__main__":
    asyncio.run(main())
