import pandas as pd
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from .sql_query import STORAGE_PATH

def get_dataset_name(user_query: str) -> str:

    load_dotenv()
    csv_file = STORAGE_PATH / "sum_dataset.csv"
    data = pd.read_csv(csv_file)

    model = ChatOpenAI(model="gpt-4o")

    template = "You are a CSV parsing assistant. Analyze the provided CSV file:{data}. Respond with the dataset_name of the dataset_context column matching the user's query.If no matching dataset exists, respond with an empty string .write only a name of dataset which can match the user input context. User query: {user_context}"

    prompt_template = ChatPromptTemplate.from_template(template)

    prompt = prompt_template.invoke({"data": data, "user_context": user_query})
    result = model.invoke(prompt)

    return result.content

if __name__ == "__main__":
    user_query = "daeth from cancer in 2023"
    respinse = get_dataset_name(user_query)
    print(respinse)
    print(len(respinse))