from __future__ import annotations
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col
import json

def hello(session: Session) -> DataFrame:
    df = session.table("pl157r.snowpark.customers")
    cdf = df.groupBy("STATE").count()
    return df 
    

if __name__ == "__main__":
    session = Session.builder.configs(json.load(open("/Users/pl157r/.snowsql/connection.json"))).create()
    print (hello (session).show())

