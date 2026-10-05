from contextlib import asynccontextmanager
from fastapi import FastAPI

import database
from tickets_router import router as tickets_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.init_db()
    yield
    
app = FastAPI(
    title ="AI Ticket Assistane",
    lifespan=lifespan
)

app.include_router(tickets_router)

@app.get('/health')
def health():
    return {"status": "ok"}