import asyncio
from time import perf_counter

import httpx2

async def main():
    async with httpx2.AsyncClient(
        base_url="http://localhost:8007",
        timeout=10.0,
    ) as client:
        for path in ["/async", "/blocking", "/sync"]:
            start = perf_counter()
            responses = await asyncio.gather(
                client.get(path),
                client.get(path),
            )
            
            for response in responses:
                response.raise_for_status()
            elapsed = perf_counter() - start
            print(f"{path}: {elapsed:.2f} seconds")

asyncio.run(main())

        