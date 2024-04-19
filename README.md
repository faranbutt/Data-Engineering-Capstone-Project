# COVID-19 Data Engineering Project   NOTE:(Infrastructure code is not uploading due to some conflicts)

This project focuses on collecting, processing, and analyzing COVID-19 data using various data engineering tools and technologies. The project employs Terraform for infrastructure setup, dbt for analytical engineering, Mage.ai for workflow orchestration and data transformation, Google Cloud Platform (GCP) BigQuery for data warehousing, PySpark for batch processing, and Confluent Kafka for real-time data processing.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Dashboard](#dashboard)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The COVID-19 pandemic has generated massive amounts of data related to infection rates, testing, hospitalizations, and more. This project aims to centralize, process, and analyze this data to provide valuable insights for healthcare professionals, policymakers, and the general public.

## Technologies Used

- **Terraform**: Infrastructure as code tool used to provision and manage the project's infrastructure on cloud platforms.
- **dbt (Data Build Tool)**: Analytics engineering tool used for transforming and modeling data in the data warehouse.
- **Mage.ai**: Workflow orchestration and data transformation platform used to streamline data processing tasks.
- **Google Cloud Platform (GCP) BigQuery**: Fully managed, serverless data warehouse used for storing and querying large datasets.
- **PySpark**: Python API for Apache Spark used for large-scale batch processing of data.
- **Confluent Kafka**: Distributed streaming platform used for real-time data processing and event streaming.
- **Docker**: Contanarization.

## Project Structure

The project is structured as follows:

covid19/
│
├── analyitcs/
│ ├── dbt/
│ │ ├── analyses/
│ │ ├── macros/
│ │ └── ...
│ └── ...
│
├── containerization/
│ ├── docker/
│ │ ├── docker-compose.yml
│ │ │ 
│ │ └── ...
│ └── ...
│
├── workflows/
│ ├── mage/
│ │ ├── export_data/
│ │ │ ├── export_to_gcp.py
│ │ ├── load_data/
│   │ ├── load_data_to_gcp.py
│ └── ...
│
│
├── kafka/
│ │── consumer.py
│ │── producer.py
└── README.md


## Setup Instructions

1. **Infrastructure Setup**: Use Terraform scripts in the `infrastructure/terraform/` directory to provision the required cloud resources. Make sure to configure your cloud provider credentials and settings.

2. **Analytical Engineering**: Utilize dbt models in the `analytics/dbt/models/` directory to transform and model data in the data warehouse.

3. **Workflow Orchestration**: Define and manage data processing workflows using Mage.ai workflows in the `workflows/mage_ai/workflows/` directory.

4. **Batch Processing**: Implement batch processing tasks using PySpark scripts in the `batch_processing/pyspark/` directory.

5. **Real-time Processing**: Develop real-time data processing pipelines using Confluent Kafka consumer and producer scripts in the `realtime_processing/confluent_kafka/` directory.

## Dashboard
 - Currently in Progress......

## Usage

- Modify and extend the provided scripts and configurations to suit your specific data processing requirements.
- Refer to individual tool documentation for detailed usage instructions and best practices.

## Contributing

Contributions to improve and expand this project are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
