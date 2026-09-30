
from huggingface_hub import snapshot_download
import os
import glob
import shutil
import pyarrow.parquet as pq


# Download the dataset from Hugging Face
data_path = snapshot_download(
    repo_id="curitibaresearch/bus-linear-interpolation",
    repo_type="dataset"
)

print("Dataset downloaded at : ")
print(data_path)


# Find all parquet files
files = glob.glob(
    os.path.join(data_path, "**", "*.parquet"),
    recursive=True
)

print(f"\nFound {len(files)} parquet files")


# These are the columns for each type of data
itinerary_cols = [
    "line_code", "itinerary_id", "latitude", "longitude",
    "name", "number", "line_way", "type", "seq", "id",
    "next_stop_id", "next_stop_latitude", "next_stop_longitude",
    "next_stop_delta_s", "max_seq"
]

tracking_cols = [
    "line_code", "itinerary_id", "vehicle",
    "event_timestamp", "id", "seq", "generated"
]


# Here we find the main project folder
project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

curitiba = os.path.join(project, "Datasets", "CuritibaResearch_Bus-linear-interpolation")

itinerary_folder = os.path.join(curitiba,"bus_itineraries")
tracking_folder = os.path.join(curitiba,"bus_tracking")

os.makedirs(itinerary_folder, exist_ok=True)
os.makedirs(tracking_folder, exist_ok=True)


# Here we check every parquet file and put it in the right folder
itinerary_count = 0
tracking_count = 0

for file in files:

    columns = pq.read_schema(file).names

    if columns == itinerary_cols:
        destination = os.path.join(
            itinerary_folder,
            os.path.basename(file)
        )

        shutil.copy2(file, destination)
        itinerary_count += 1

    elif columns == tracking_cols:
        destination = os.path.join(
            tracking_folder,
            os.path.basename(file)
        )

        shutil.copy2(file, destination)
        tracking_count += 1


print("\nDone!")

print(f"Bus itinerary files : {itinerary_count}")
print(f"Bus tracking files : {tracking_count}")

print("\nFiles saved here : ")
print(itinerary_folder)
print(tracking_folder)