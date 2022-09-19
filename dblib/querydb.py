

from databricks import sql
import os
import pandas as pd


def querydb():
    query = "SELECT * FROM default.new_test_csv"
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            df = pd.DataFrame(row)
            print(df)

    return result