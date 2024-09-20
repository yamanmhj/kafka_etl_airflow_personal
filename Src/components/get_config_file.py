import yaml
import os

def get_config_file_from_path(currentdirectory):
     config_path = os.path.join(currentdirectory, 'config', 'config.yaml')
     with open(config_path, 'r') as file:
        config_data = yaml.safe_load(file)
        return config_data
     
def get_csv_data_from_LOadConsumerData():
    for file in os.listdir(os.getcwd(),):
            if file.endswith('.csv'):
                file_path = os.path.join(self.csv_directory, file)
                df = pd.read_csv(file_path)
                data_frames.append(df)