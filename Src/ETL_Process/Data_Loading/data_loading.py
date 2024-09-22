import yaml
from io import StringIO
import boto3
import sys

from Components.get_config_file import get_config_Full_file
from Data_Extraction.data_extraction import DataExtractorclass
from Data_Transformation.data_transformation import DataTransformerclass

def create_s3_client(Aws_Access_key, Aws_Secret_Key, AWS_Region_Name):
    return boto3.client('s3',
                        aws_access_key_id=Aws_Access_key,
                        aws_secret_access_key=Aws_Secret_Key,
                        region_name=AWS_Region_Name)

def create_directories_in_s3(s3_client, bucket_name, *directories):
    for directory in directories:
        s3_client.put_object(Bucket=bucket_name, Key=(directory + '/'))

def upload_files_in_s3(s3_client, bucket_name, data_frames, directory):
    for i, df in enumerate(data_frames):
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        file_name = f'{directory}/file_{i + 1}.csv'
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())

def load_data_to_s3():
    full_config_file = get_config_Full_file()
    directory_of_csv = full_config_file['StoreApiDataIn']
    aws_access_key = full_config_file['Aws_Access_key']
    aws_secret_key = full_config_file['Aws_Secret_key']
    aws_bucket_name = full_config_file['AWS_Bucket_Name']
    aws_region_name = full_config_file['AWS_Region_Name']

    s3_client = create_s3_client(aws_access_key, aws_secret_key, aws_region_name)

    # Assuming the data extraction and transformation processes
    extracted_dataframe = DataExtractorclass().extract_csv_from_folder()
    transformed_dataframe = DataTransformerclass(extracted_dataframe)

    create_directories_in_s3(s3_client, aws_bucket_name, 'Kafka')
    upload_files_in_s3(s3_client, aws_bucket_name, transformed_dataframe, 'Kafka')

