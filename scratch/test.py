import requests
import pandas as pd

# response = requests.get("https://api.weather.gov")
# print(response)

df = pd.read_csv("../data/worldcities.csv")
print(df)
