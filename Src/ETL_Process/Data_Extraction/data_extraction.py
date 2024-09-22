import os
from os.path import dirname, abspath
import pandas as pd
import sys

from Components.get_config_file import get_config_Full_file

class DataExtractorclass:
    def __init__(self):
        pass

    def extract_csv_from_folder(self):
        data_frames = []
        config_full_file = get_config_Full_file()
        csv_Path_Location = config_full_file['StoreApiDataIn']
        print("Path Location is", csv_Path_Location)
        
        # Loop through the files in the directory
        for file in os.listdir(csv_Path_Location):
            if file.endswith('.csv'):
                new_file_path = os.path.join(csv_Path_Location, file) 
                df = pd.read_csv(new_file_path)
                data_frames.append(df)

        return data_frames


