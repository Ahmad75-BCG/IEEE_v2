import pandas as pd

def process_energy_data(raw_data):
    # Logic to normalize Wi-Fi occupancy or IoT sensor data
    df = pd.DataFrame(raw_data)
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df