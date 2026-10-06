import asyncio
from time import perf_counter

async def fetch_data(name: str):
    print(f"{name}: start fetching data...")
    await asyncio.sleep(2)
    print(f"{name}: done fetching data!")
    return name

async def main():
    print("\n synchronous execution:")
    start = perf_counter()

    await fetch_data("Task 1")
    await fetch_data("Task 2")

    print(f"Total time taken: {perf_counter() - start:.2f} seconds")

    print("\n asynchronous execution:")
    start = perf_counter()
    result = await asyncio.gather(fetch_data("Task 1"), fetch_data("Task 2"))
    print(f"Results: {result}")
    print(f"Total time taken: {perf_counter() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())