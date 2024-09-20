import os
from os.path import dirname, abspath
import pandas as pd
from  components.get_config_file import get_config_file_data_from_path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(abspath(__file__))), 'src'))


class ExtractDataandconfigyaml:
    def __init__(self, consumer_data_directory):
        self.consumer_data_directory = consumer_data_directory



    def extract_csv_from_folder(self):
        data_frames = []
        csv_Path = os.path.join(os.getcwd(),'LoadCustomerData')
        for file in os.listdir(csv_Path):
            if file.endswith('.csv'):
                file_path = os.path.join(csv_Path, file)
                df = pd.read_csv(file_path)
                data_frames.append(df)
                
        return data_frames


