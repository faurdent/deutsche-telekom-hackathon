from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent import AgentExecutor
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
from langchain_community.agent_toolkits import create_sql_agent
from pathlib import Path
import pandas as pd

load_dotenv()

STORAGE_PATH = Path(__file__).parent.parent / "data" 
llm = ChatOpenAI(model="gpt-4o-mini")


def csv_to_sql(csv_name) -> None:
    csv_path = csv_name + ".csv"
    df = pd.read_csv(STORAGE_PATH / "datasets" / csv_path)

    engine = create_engine(f"sqlite:///{STORAGE_PATH / csv_name}.db")
    if sqlalchemy.inspect(engine).get_table_names():
        return
    
    df.to_sql(csv_name, engine, index=False)


def create_agent_executor(llm, db_name, agent_type="openai-tools", verbose=False) -> AgentExecutor:
    engine = create_engine(f"sqlite:///{STORAGE_PATH / db_name}.db")
    db = SQLDatabase(engine=engine)
    agent_executor = create_sql_agent(llm, db=db, agent_type=agent_type, verbose=verbose)
    return agent_executor


async def get_sql_answer(question: str, db_name: str):
    return await create_agent_executor(llm, db_name).ainvoke({"input": question})


def setup_databases():
    datasets_dir = STORAGE_PATH / "datasets"
    for dataset in datasets_dir.iterdir():
       print(dataset)
       csv_to_sql(dataset.stem.strip(".csv"))
