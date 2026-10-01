import logging
import os
import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_HOST = os.getenv("DBHOST")
DB_NAME = os.getenv("DBNAME")
DB_USER = os.getenv("DBUSER")
DB_PASSWORD = os.getenv("DBPASS")




def read_data(filename):
    """Read data from a CSV file into a DataFrame."""
    logger.info("Reading data from %s", filename)
    df=pd.read_csv(filename)
    return df

def clean_data(df):
    """Remove rows with missing values from the DataFrame"""
    logger.info("Cleaning data")
    return df.dropna()

def load_data(df, table):
    """Use engine to connect and load data in SQL"""
    try:
        connection_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
        engine = create_engine(connection_url)
        df.to_sql(table, engine, if_exists="append", index=False)
        logger.info("Data loaded successfully")
    except Exception as e:
        logger.error("Error loading data: %s", e)
    


def main():
    """Actually run functions with MOCK_DATA CSV"""
    df = read_data("MOCK_DATA.csv")
    df = clean_data(df)
    load_data(df, "mock")
    logger.info("Main function ran successfully")

if __name__ == "__main__":
    main()





