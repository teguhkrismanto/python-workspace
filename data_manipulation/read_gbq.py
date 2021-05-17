import pandas as pd

query = """
SELECT * FROM 'bigquery-public-data.covid19_jhu_csse_eu.summary'
LIMIT 1000
"""

df_covid19_eu_summary = pd.read_gbq(query, project_id = "XXX")
df_covid19_eu_summary