import mysql.connector
import pandas as pd

my_conn = mysql.connector.connect(host = "localhost",
                                port = 3306,
                                user = "GUEST",
                                passwd = "PASSWORD",
                                database = "DATABASE",
                                use_pure = True)

my_query = """
SELECT * FROM table_name
"""

df = pd.read_sql_query(my_query, my_conn)
df.head()