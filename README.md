![kafka](https://github.com/user-attachments/assets/ee0abc6c-e81a-43b9-b84f-da3599961a4a)
# ETL Pipeline with Kafka and Airflow

This project demonstrates an **ETL (Extract, Transform, Load) pipeline** that leverages **Apache Kafka** and **Apache Airflow** to extract data from an API, transform it, and load it into a local storage system. The project uses **Docker** to orchestrate Kafka and Airflow environments seamlessly.

---

## Features

- **Kafka Integration**: Utilized Kafka for real-time data ingestion from APIs.
- **Airflow ETL Orchestration**: Automates extraction, transformation, and loading operations.
- **Resource Optimization**: Data is stored locally to minimize unnecessary cloud storage costs.
- **Dockerized Setup**: Ensures reproducibility and easy deployment with Docker containers for Kafka and Airflow.

---

## Project Structure

```

- LoadConsumerData
- Logger.py
- Logs
- Src
  - Components
    - get_config_file.py
  - Dags
  - ETL_Process
    - Data_Extraction
      - data_extraction.py
    - Data_Loading
      - data_loading.py
    - Data_Transformation
      - data_transformation.py
  - KAFKA
    - consumer.py
    - producer.py
  - __init__.py
  - __pycache__
    - exceptionhandling.cpython-312.pyc
  - exceptionhandling.py
- config
  - config.yaml
- docker-compose.yaml
- mlfullpipeline.egg-info
  - PKG-INFO
  - SOURCES.txt
  - dependency_links.txt
  - top_level.txt
- plugins
- requirements.txt
- setup.py
- utils.py
---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose
- Python 3.8 or higher

### Installation

1. Install Python dependencies:

   pip install -r requirements.txt
  

2. Configure the `config/config.yaml` file with the API details and other ETL settings.

---

## Usage

1. **Run Kafka and Airflow**:
   Ensure Kafka and Airflow containers are running using Docker Compose:

   ```bash
   docker-compose up -d
   ```

2. **Trigger the ETL Pipeline**:
   Use the Airflow UI to trigger the DAG:

   - Access the Airflow web server at `http://localhost:8080`
   - Enable and trigger the ETL DAG.

3. **Monitor Logs**:
   Check the `logs/` folder for detailed execution logs.

4. **Verify Output**:
   Processed data will be saved in the `artifacts/` directory.

---

## Modules Overview

### API Extraction

- Connects to the API to fetch raw data.
- Handles pagination and error scenarios during data retrieval.

### Data Transformation

- Cleans and transforms the raw data into a structured format.
- Ensures compatibility with downstream systems.

### Local Loader

- Stores transformed data into the local storage system under the `artifacts/` directory.

#### Airflow DAG

- # Orchestrates the ETL process by triggering tasks for extraction, transformation, and loading.
- # Configured with retries and failure alerts.
- # We can also schedule the ETL pipeline on when and where to run it

---

## Configuration

Edit the `config/config.yaml` file to customize API endpoints, Kafka topics, and ETL settings. Example:

kafka:
  topic: "etl_topic"
  bootstrap_servers: "localhost:9092"

etl:
  batch_size: 100
  output_path: "./artifacts/"
```


