# !pip install SQLAlchemy

import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

engine = create_engine('sqlite:///inventory.db')


def ingest_db(df, table_name, conn):
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        logging.info(f"Successfully ingested data into {table_name} table, replacing existing table if any.")
    except Exception as e:
        logging.error(f"Error during data ingestion into {table_name}: {e}")
        
def load_raw_data():
    start = time.time()
    for file in os.listdir('datasets'):
        if '.csv' in file:
            df = pd.read_csv('datasets/' + file)
            logging.info(f'Ingesting {file} in db')
            # print(df.shape)
            ingest_db(df,file[:-4], engine)
    end = time.time()
    total_time_taken = (end - start)/60
    logging.info('INGESTION COMPLETE')
    logging.info(f'\nTotal Time Taken: {total_time_taken} minutes')

if __name__ == '__main__':
    load_raw_data()