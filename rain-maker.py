import datetime
import json

import pandas as pd
import requests

# Get today's date
thisday = datetime.datetime.now()
ten_days_ago = thisday - datetime.timedelta(days=10)
# Format the date as YYYY-MM-DDTHH:MM:SSZ
formatted_date = ten_days_ago.strftime("%Y-%m-%dT%H:%M:%SZ")
print("ten days ago :" + formatted_date)

# URL of the REST API
# https://environment.data.gov.uk/flood-monitoring/id/stations/305111/readings?since=2024-05-13T10:30:00Z&_limit=1000
url = "http://environment.data.gov.uk/flood-monitoring/id/stations/305111/readings?since=" + formatted_date + "&_limit=1000"

# Send GET request
response = requests.get(url)

# Parse the JSON response
jsondata = json.loads(response.text)
# empty list to hold the data from joson

new_list = []
# Open a CSV file for writing
# define the data folder path
maincsv_path = r"C:\temp\ukea-rainfall-data-grabber\data\rawdata.csv"

for item in jsondata["items"]:
    date_time = item["dateTime"]
    date_only = date_time[:10]
    measure = item["measure"]
    value = item["value"]

    # Append the row to the list
    new_list.append([date_time, date_only, measure, value])
    # print(dateTime, measure, value)

new_data = pd.DataFrame(new_list, columns=["datetime", "date", "measure", "value"])
# new_data.set_index("dateTime", inplace=True)

# Load the CSV data into a DataFrame
try:
    df = pd.read_csv(maincsv_path)
    df.columns = ["datetime", "date", "measure", "value"]
    df.reset_index(drop=True, inplace=True)
except:
    df = pd.DataFrame(columns=["datetime", "date", "measure", "value"])


# Append new data
merged_df = pd.merge(df, new_data, how="outer")

merged_df.drop_duplicates(keep="last", inplace=True)

# Save the updated DataFrame back to CSV
merged_df.to_csv(maincsv_path, index=False)

# Futher process the dataframe, group values by date and sum the 15min reading by date
day_df = merged_df.groupby(merged_df.columns[1])[merged_df.columns[3]].sum().reset_index()
day_df.drop(day_df.tail(2).index, inplace=True)
processedcsv_path = r"C:\temp\ukea-rainfall-data-grabber\data\processed_data.csv"

# Read the processed_data.csv file first so historic entries (manual entries) can be preserved
histo_df = pd.read_csv(processedcsv_path, index_col=False)
stack_df = pd.concat([histo_df, day_df])
stack_df.drop_duplicates(inplace=True, ignore_index=True)
stack_df.reset_index(drop=True, inplace=True)
stack_df.to_csv(processedcsv_path, index=False)
