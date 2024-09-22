import yaml
import os

def get_config_Full_file():
    module_dir = os.path.dirname(__file__)
    config_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(module_dir)), 'config', 'config.yaml'))
    
    # Load and return the config data
    with open(config_path, 'r') as file:
        config_file_data = yaml.safe_load(file)

    print("config_data is", config_file_data)

    return config_file_data