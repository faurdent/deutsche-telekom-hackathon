from contextlib import asynccontextmanager

from fastapi import FastAPI
from schemas import Message
from utils import get_sql_answer, setup_databases


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_databases()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/get-analytics")
async def get_analytics(message: Message):
    #db_name = get_database_name()
    db_name = "SPI_index"
    sql_answer = await get_sql_answer(message.text, db_name)
    return sql_answer

