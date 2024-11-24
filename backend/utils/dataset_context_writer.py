import pandas as pd
import csv
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from .sql_query import STORAGE_PATH


def get_dataset_description(csv_file: str) -> str:

    load_dotenv()
    data = pd.read_csv(csv_file)
    data = data[:50]
    model = ChatOpenAI(model="gpt-4o", temperature=0)

    template = "You are a CSV parsing assistant. Analyze the provided CSV file:{data}. You need to analyzeprovided csv and based on the data, you need to write short context about the data. Make it short and clear and wrrite it all in one line"

    prompt_template = ChatPromptTemplate.from_template(template)

    prompt = prompt_template.invoke({"data": data})
    result = model.invoke(prompt)

    return result.content


def write_new_row(csv_file : str):
    response = get_dataset_description(csv_file)
    with open( STORAGE_PATH / "sum_dataset.csv", mode="a", newline='') as file:
        csv.writer(file).writerow([f'{csv_file.stem.split('/')[-1].replace(".csv", "")}', response])


if __name__ == "__main__":
    csv_file = "backend/data/datasets/UNdata_Export_20241124_044258778.csv"
    write_new_row(csv_file)
