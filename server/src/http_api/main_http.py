from .routers.sc_router import sc_router
from db.database import init_tables
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

@asynccontextmanager
async def lifespan(app : FastAPI):
    await init_tables()
    print("Db init...")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(sc_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app,port=8181)
    