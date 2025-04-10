from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.engine import create_table
from fastapi.middleware.cors import CORSMiddleware
from app.user.router.user_router import user_router
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    yield
    print("Выключение")
    
    
app = FastAPI(lifespan=lifespan)


app.include_router(user_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:8000"]
)


if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)