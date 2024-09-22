import pandas as pd

class DataTransformerclass:
    def __init__(self):
        pass

    def transformkafka(self,data_frames):
        transformed_data_frames_kafka = []
        for df in data_frames:
            # Convert 'dob' column to datetime format
            df['dob'] = pd.to_datetime(df['dob'])

            # Extract year, month, day, and hour from 'dob' column
            df['dob_year'] = df['dob'].dt.year
            df['dob_month'] = df['dob'].dt.month
            df['dob_day'] = df['dob'].dt.day
            df['dob_hour'] = df['dob'].dt.hour

            # Append transformed dataframe to the list
            transformed_data_frames_kafka.append(df)
        
        return transformed_data_frames_kafka
