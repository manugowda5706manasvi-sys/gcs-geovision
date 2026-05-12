from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="AI Smart Campus Security System",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
def read_root():
    return {
        "message": "AI Smart Campus Security System backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "backend",
        "database": "connected"
    }