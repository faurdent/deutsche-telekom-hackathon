import pandas as pd
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def get_dataset_columns(csv_file: str, usr_q : str) -> str:

    load_dotenv()
    data = pd.read_csv(csv_file)
    data = data[:50]
    model = ChatOpenAI(model="gpt-4o", temperature=0)

    template = """
    You have acces to pandas DataFrame df.
    Here are some example line from table.

    {data}

    Return two name of a columns which will be used for dataanalyze.Writeonly a name of column like this: "column_name,column_name" always retun 2 columns and do not write anything else. Write only a column names. based on the user question below:
    {usr_q}

    ALWAYS RETUNRN 2 DIFFERENT COLUMNS LIKE THIS: "column_name,column_name"
    """

    prompt_template = ChatPromptTemplate.from_template(template)

    prompt = prompt_template.invoke({"data": data, "usr_q" : usr_q})

    column_name = model.invoke(prompt)
    return column_name.content

def get_columns(csv_file: str, usr_q : str) -> str:
    response = get_dataset_columns(csv_file, usr_q)
    try:
        response = response.replace("\'",'').replace("\"",'').split(",")
        data = pd.read_csv(csv_file)
        return [{'x': x, 'y': y} for x, y in zip(data[response[0]], data[response[1]])]
    except Exception as e:
        return []


if __name__ == "__main__":
    csv_file = "backend/data/datasets/time_series_covid19_deaths_global.csv"
    question = "How many people diied from covid in 2029.14.14"
    print(get_columns(csv_file, question))
