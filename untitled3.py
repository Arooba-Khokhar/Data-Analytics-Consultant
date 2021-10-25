import requests
import pandas as pd
import time
import io
from datetime import datetime,date,timedelta
from google.cloud import bigquery
def main():

    #csvResponse = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/cs
#se_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.c
#sv').text
pd = pd.read_csv('time_series_covid19_confirmed_global.csv')

pd=pandas.read_csv(io.StringIO(csvResponse))
pd.drop(["Province/State",'Lat','Long'],axis=1,inplace=True)
pd=pd.rename(columns={"Country/Region": "Country"})
# do the unpivoting here ...


pd = pd.melt(id_vars=['Country'], var_name='Date')
6pd


# ignore BigQuery Loading for this test
# client = bigquery.Client()
# table_id='f-26914.test_covid.confirmed'
# job_config = bigquery.LoadJobConfig(
# write_disposition="WRITE_TRUNCATE"
# )
# job = client.load_table_from_dataframe(
# pd,
# table_id,
# job_config=job_config,
# location="europe-west3",
# )
# job.result()
main()