import asyncio
import time

from fastapi import FastAPI

app = FastAPI()

@app.get("/async")
async def await_async():
    await asyncio.sleep(2)
    return {"type": "async"}

@app.get("/blocking")
async def await_blocking():
    time.sleep(2)
    return {"type": "blocking"}

@app.get("/sync")
def wait_sync():
    time.sleep(2)
    return {"type": "sync"}