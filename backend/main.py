from fastapi import FastAPI
from schemas import Message

app = FastAPI()


@app.post("/get-analytics")
async def get_analytics(message: Message):
    pass
