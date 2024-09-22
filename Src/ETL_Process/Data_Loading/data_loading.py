import yaml
from io import StringIO
import boto3
import sys
from Components.get_config_file import get_config_Full_file
from ETL_Process.Data_Extraction import data_extraction
from ETL_Process.Data_Transformation import data_transformation

from Data_Extraction.data_extraction import DataExtractorclass
from Data_Transformation.data_transformation import DataTransformerclass

class S3Loader:
    def __init__(self, AWS_Bucket_Name,Aws_Access_key, Aws_Secret_Key,AWS_Region_Name):
        self.s3_client = boto3.client('s3',
                                      aws_access_key_id = Aws_Access_key,
                                      aws_secret_access_key = Aws_Secret_Key,
                                      region_name=AWS_Region_Name)
        self.bucket_name = AWS_Bucket_Name

    def create_directories_in_s3(self,*directories):
        for directory in directories:
            self.s3_client.put_object(Bucket = self.bucket_name, key = (directory+'/'))

    def upload_files_in_s3(self, data_frames, directory):
        for i, df in enumerate(data_frames):
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index = False)
            file_name = f'{directory}/file_{i+1}.csv'
            self.s3_client.put_object(Bucket=self.bucket_name, Key = file_name, Body =csv_buffer.getvalue())




def main():
    full_config_file = get_config_Full_file()
    Directory_of_csv = full_config_file['StoreApiDataIn']
    Aws_Access_key = full_config_file['Aws_Access_key']
    Aws_Secret_Key = full_config_file['Aws_Secret_key']
    AWS_Bucket_Name = full_config_file['AWS_Bucket_Name']
    AWS_Region_Name =full_config_file['AWS_Region_Name']

    loader = S3Loader(AWS_Bucket_Name,Aws_Access_key, Aws_Secret_Key,AWS_Region_Name)

    extracted_dataframe = DataExtractorclass().extract_csv_from_folder

    transformed_dataframe = DataTransformerclass(extracted_dataframe)

    loader.create_directories_in_s3('Kafka')
    loader.upload_files_in_s3(transformed_dataframe,'Kafka')
