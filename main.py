from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import chat

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://localhost",
    "https://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)