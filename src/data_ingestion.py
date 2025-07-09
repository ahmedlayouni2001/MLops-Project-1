import pandas as pd

def load_weather_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f" Successfully loaded data with shape: {df.shape}")
        print(f" Columns: {list(df.columns)}")
        
        # Optionally parse datetime if a timestamp column exists
        if 'valid_time' in df.columns:
            df['valid_time'] = pd.to_datetime(df['valid_time'])
        
        return df
    
    except Exception as e:
        print(f" Error loading data: {e}")
        return None
