from contextlib import asynccontextmanager

from fastapi import FastAPI, UploadFile, File, Form
from schemas import Message
from utils import (get_sql_answer, setup_databases, get_dataset_name, 
                   add_dataset, csv_to_sql, write_new_row, STORAGE_PATH, get_columns)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_databases()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/get-analytics")
async def get_analytics(
    # save_file: bool, 
    text: str = Form(),
                        # file: UploadFile | None = File(None)
                    ):
    
    # await add_dataset(file)
    # csv_to_sql(file.filename)
    # path = STORAGE_PATH / "datasets" / file.filename
    # if file != 0:
        # write_new_row(path)
        # sql_answer = await get_sql_answer(text, file.filename)
        # if not save_file:
        #     path.unlink()
        #     STORAGE_PATH.joinpath(f"{file.filename}.db").unlink()
        # return sql_answer

    db_name = get_dataset_name(text)
    print(db_name)
    if not db_name:
        return "We don't have data to help you, but you can upload own dataset.", []
    return await get_sql_answer(text, db_name), get_columns(STORAGE_PATH / "datasets" / f"{db_name}.csv", text)
