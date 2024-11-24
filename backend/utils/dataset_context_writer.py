import pandas as pd
import csv
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def get_dataset_name(csv_file: str) -> str:

    load_dotenv()
    data = pd.read_csv(csv_file)
    data = data[:50]
    model = ChatOpenAI(model="gpt-4o", temperature=0)

    template = "You are a CSV parsing assistant. Analyze the provided CSV file:{data}. You need to analyzeprovided csv and based on the data, you need to write short context about the data. Make it short and clear"

    prompt_template = ChatPromptTemplate.from_template(template)

    prompt = prompt_template.invoke({"data": data})
    result = model.invoke(prompt)

    return result.content


def write_new_row(csv_file : str):
    response = get_dataset_name(csv_file)
    with open("backend/data/sum_dataset.csv", mode="a", newline='') as file:
        csv.writer(file).writerow([f'{csv_file.split('/')[-1].replace(".csv", "")}',response])

if __name__ == "__main__":
    csv_file = "backend/data/datasets/time_series_covid19_deaths_global.csv"
    write_new_row(csv_file)
