import requests
import pandas as pd
from google.transit import gtfs_realtime_pb2
from datetime import datetime
import os


# Connect to the Delhi real-time API
api_key = "PWcxa0qGrvXuWNzFR69AawCx9pObDM0U"
url = ("https://otd.delhi.gov.in/api/realtime/" f"VehiclePositions.pb?key={api_key}")


# Find the project folder
project = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

folder = os.path.join(project, "Datasets", "Delhi Bus Transit Data")
os.makedirs(folder, exist_ok=True)


# Download the data
print("Downloading Delhi bus data...")

response = requests.get(url, timeout=30)
if response.status_code != 200:
    print("API Error:", response.status_code)
    print(response.text)
    exit()
print("Download successful!")


# Read the actual GTFS-RT response
feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(response.content)


# Extract whatever is actually present
rows = []

for entity in feed.entity:
    if not entity.HasField("vehicle"):
        continue
    vehicle = entity.vehicle

    row = {"entity_id": entity.id}

    # Get every field defined in the vehicle message
    for field, value in vehicle.ListFields():

        name = field.name

        if field.message_type is not None:

            # Handle nested messages such as vehicle, trip and position
            for sub_field, sub_value in value.ListFields():

                row[f"{name}_{sub_field.name}"] = str(sub_value)
        else:
            row[name] = value

    rows.append(row)


# Put the extracted data into a CSV
df = pd.DataFrame(rows)

now = datetime.now()

filename = now.strftime("Delhi Bus - %d %b %Y – %-I:%M %p.csv")

filepath = os.path.join(folder, filename)

df.to_csv(filepath, index=False)

print("\nNumber of records:", len(df))
print("Columns found:")
print(df.columns.tolist())

print("\nCSV saved:")
print(filepath)

print("\nDone!")