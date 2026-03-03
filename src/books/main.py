from fastapi import FastAPI, HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db
import uvicorn

@asynccontextmanager
async def life_span(app:FastAPI):
    await init_db()
    yield
    print('Server has been stopped')

version = 'v1'

app = FastAPI(
    title = 'Bookly',
    version= version,
    description = "REST API for book service",
    lifespan = life_span
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://restfox.dev"],  # Allows all origins; change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # Allows all headers
)

app.include_router(book_router, prefix = f'/api/{version}/books', tags = ['books'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


