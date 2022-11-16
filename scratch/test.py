import requests
import pandas as pd

response = requests.get(
    "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
)
# print(response.json())
out = pd.DataFrame(
    [response.json()["hourly"]["time"], response.json()["hourly"]["temperature_2m"]]
).T
out.columns = ["hour", "temp"]

out["hour"] = pd.to_datetime(out["hour"])
print(out.dtypes)
out.to_csv("output.csv")
