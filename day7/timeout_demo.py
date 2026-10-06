import asyncio
from time import perf_counter

import httpx2

async def main():
    async with httpx2.AsyncClient(
        base_url="http://127.0.0.1:8007",
    ) as client:
        
        for timeout_seconds in [1.0, 3.0]:
            print(f"Timeout: {timeout_seconds} seconds")
            start = perf_counter()
            try:
                response = await client.get(
                    "/async",
                    timeout=timeout_seconds,
                )
                response.raise_for_status()
                print(f"success: {response.json()}")
            
            except httpx2.TimeoutException:
                print("timeout", type(error).__name__)
                
            except httpx2.HTTPStatusError as error:
                print("http error", type(error).__name__, error.response.status_code)
            except httpx2.RequestError as error:
                print("other error", type(error).__name__, str(error))
            
            elapsed = perf_counter() - start
            print(f"Elapsed time: {elapsed:.2f} seconds")

asyncio.run(main())