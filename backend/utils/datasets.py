from fastapi import File

from .sql_query import STORAGE_PATH
from .dataset_context_writer import write_new_row


async def add_dataset(csv_file: File):
    with open(STORAGE_PATH / "datasets" / csv_file.filename, "wb") as file:
        content = await csv_file.read()
        file.write(content)
