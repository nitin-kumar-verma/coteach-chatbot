from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn

from app.api import chatbot

load_dotenv()
app = FastAPI()


@app.get('/')
async def root():
    return "Welcome"

app.include_router(chatbot.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)