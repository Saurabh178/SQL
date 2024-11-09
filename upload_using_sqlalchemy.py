import warnings
from urllib.parse import quote
import pandas as pd
from sqlalchemy import create_engine

warnings.filterwarnings('ignore')

#credentials
user='root'
password=quote('178@SAurabh')
db_Name='Flights'
host='127.0.0.1:3306'

try:
    engine=create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db_Name}", echo=True)
    conn=engine.connect()
    table_name='airport'

    #upload data to sql
    data=pd.read_csv('flights_cleaned - flights_cleaned.csv')
    data.to_sql(table_name, engine, index=False, if_exists='replace')

    #read SQL table
    data=pd.read_sql_table(table_name, con=engine)
    print("Read Data successful!")
    print(data.head())

except Exception as e:
    print("An error occurred:", e)

finally:
    conn.close()
