# Curitiba Bus Linear Interpolation Dataset

> [!IMPORTANT]
> This dataset is **very large (~5.1 GB total)** and is **not committed to Git**.
> It is stored on **Google Drive**. See the access details below.

---

## 📦 Storage & Access

| Detail | Info |
|--------|------|
| **Stored on** | Google Drive (shared folder) |
| **Google Drive Link** | *(add your Google Drive link here)* |
| **Original Source** | [HuggingFace — curitibaresearch/bus-linear-interpolation](https://huggingface.co/datasets/curitibaresearch/bus-linear-interpolation) |
| **Gitignored** | ✅ Yes — `bus_itineraries/` and `bus_tracking/` are excluded from version control |

---

## 🗂️ Folder Structure

```
Curitibaresearch_Bus-linear-interpolation/
├── README.md                        ← you are here (committed to Git)
├── bus_itineraries/                 ← 1,303 parquet files (~953 MB) — gitignored
│   └── part-00000-*.snappy.parquet
└── bus_tracking/                    ← 1,224 parquet files (~4.1 GB) — gitignored
    └── part-00000-*.snappy.parquet
```

---

## 📊 Dataset Summary

| Property | `bus_itineraries` | `bus_tracking` |
|----------|-------------------|----------------|
| **Files** | 1,303 parquet | 1,224 parquet |
| **Total size** | ~953 MB | ~4.1 GB |
| **Format** | Snappy-compressed Parquet | Snappy-compressed Parquet |
| **City** | Curitiba, Brazil | Curitiba, Brazil |
| **System** | BRT (Bus Rapid Transit) | BRT (Bus Rapid Transit) |
| **Time period** | — | 2020 onwards |
| **Data type** | Route & stop geometry | Interpolated GPS tracking |

---

## 🏛️ Schema

### `bus_itineraries/` — Route & Stop Geometry

| Column | Type | Description |
|--------|------|-------------|
| `line_code` | string | Bus line identifier (e.g. `010`, `X31`, `Z01`) |
| `itinerary_id` | int | Unique itinerary (direction) ID |
| `latitude` | float | Stop latitude (WGS84) |
| `longitude` | float | Stop longitude (WGS84) |
| `name` | string | Stop name |
| `number` | string | Stop number |
| `line_way` | string | Direction of travel |
| `type` | string | Stop type |
| `seq` | int | Stop sequence number along the route |
| `id` | int | Stop ID |
| `next_stop_id` | int | ID of the next stop |
| `next_stop_latitude` | float | Latitude of the next stop |
| `next_stop_longitude` | float | Longitude of the next stop |
| `next_stop_delta_s` | float | Distance to the next stop (metres) |
| `max_seq` | int | Total number of stops in this itinerary |

### `bus_tracking/` — Interpolated GPS Tracking

| Column | Type | Description |
|--------|------|-------------|
| `line_code` | string | Bus line identifier |
| `itinerary_id` | int | Itinerary (direction) ID |
| `vehicle` | string | Vehicle ID (e.g. `BB302`) |
| `event_timestamp` | datetime | Timestamp of the interpolated position (UTC) |
| `id` | int | Stop segment ID |
| `seq` | int | Sequence position within the itinerary |
| `generated` | bool | `True` if the point was **interpolated** (not a raw GPS ping) |

> [!TIP]
> The `generated` column is key for this project — `True` rows are the linearly interpolated
> positions between raw GPS pings. Use `generated == False` to filter for actual observations.

---

## ⚙️ How to Get the Data

### Option 1 — From Google Drive
Download the folder from the shared Google Drive link above and place the contents so the structure matches the layout shown above.

### Option 2 — Re-download from HuggingFace
Run the dataset script from the project root:

```bash
.venv/bin/python3 "Code/Dataset – Curitiba Bus Linear Interpolation.py"
```

This will:
1. Download the dataset from HuggingFace into your local cache
2. Read the schema of every parquet file
3. Copy each file into `bus_itineraries/` or `bus_tracking/` based on its columns

> [!NOTE]
> The download requires ~5 GB of free disk space and an active internet connection.
> Packages required: `huggingface_hub`, `pyarrow` (both in `requirements.txt`).

---

## 🔬 How This Dataset Is Used in the Project

| Task | Folder used |
|------|-------------|
| Route shape reconstruction | `bus_itineraries/` — stop positions + `next_stop_delta_s` for cumulative distance |
| GPS trajectory analysis | `bus_tracking/` — `event_timestamp` + `seq` per vehicle per trip |
| Dwell time extraction (`DwellTimeExtractor`) | Both — match tracking points to stop boundaries from itineraries |
| Travel time estimation model | `bus_tracking/` — inter-stop travel times derived from interpolated trajectory |

---

## 🔗 References

- HuggingFace dataset card: https://huggingface.co/datasets/curitibaresearch/bus-linear-interpolation
- Key paper: *"Potential of Low-Frequency Automated Vehicle Location Data for Monitoring and Control of Bus Performance"* (Yang et al.)
- Used in: **DTUMOS** — Digital Twin for Urban Mobility Systems
