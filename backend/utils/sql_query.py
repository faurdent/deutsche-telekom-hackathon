from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from dotenv import load_dotenv
from langchain_community.agent_toolkits import create_sql_agent
from pathlib import Path
import os
import pandas as pd
import getpass



load_dotenv()


STORAGE_PATH = Path(__file__).parent.parent / "data" 
llm = ChatOpenAI(model="gpt-4o-mini")
# engine = create_engine(f"sqlite:///{DATABASE_PATH}")


def csv_to_sql(csv_name):

    csv_path = csv_name + ".csv"
    df = pd.read_csv(STORAGE_PATH/"datasets"/csv_path)
    engine = create_engine(f"sqlite:///{STORAGE_PATH / csv_name}.db")
    # TODO: Remove the if_exists="replace" later
    df.to_sql("SPI_index", engine, index=False, if_exists="replace")
    




def create_agent_executor(llm, csv_name, agent_type="openai-tools", verbose=False):
    engine = create_engine(f"sqlite:///{STORAGE_PATH / csv_name}.db")
    db = SQLDatabase(engine=engine)
    agent_executor = create_sql_agent(llm, db=db, agent_type=agent_type, verbose=verbose)
    return agent_executor



def main():
    # db = csv_to_sql("SPI_index")

    agent_executor = create_agent_executor(llm, "SPI_index")
    answer = agent_executor.invoke({"input": "what is population of Denmark"})
    print(answer)



if __name__ == "__main__":
    main()