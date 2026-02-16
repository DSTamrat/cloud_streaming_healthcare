 Cloud-Based ETL & Real‑Time Streaming Pipeline for Healthcare Admissions

This repository showcases two major data engineering workflows built using synthetic healthcare admissions data:

             A cloud‑ready ETL pipeline for batch analytics
             A real‑time streaming pipeline using Kafka + Python

Together, they demonstrate how modern healthcare systems ingest, clean, transform, and stream data for analytics, dashboards, and machine learning.

                            Project Overview

This project contains two integrated pipelines:

I - Cloud ETL Pipeline (Batch Processing)

A complete Extract–Transform–Load workflow that processes 1000 synthetic healthcare admission records.

ETL Steps

1. Ingest

Loads raw synthetic healthcare admissions data generated programmatically.

2. Clean
Removes duplicates

Handles missing values

Fixes invalid values

Standardizes data types

Adds derived fields (year, month, elderly flag)

3. Transform
Aggregates metrics by:

Hospital unit

Primary condition

Metrics include:

Admissions count

Average length of stay

Readmission rate

Average cost

4. Load
Outputs:

data_processed/healthcare_admissions_clean.csv

data_processed/healthcare_aggregated_metrics.csv

These are ready for:

Power BI dashboards

Tableau visualizations

Machine learning models

II  Real‑Time Streaming Pipeline — Kafka + Python Producer

This module simulates real‑time healthcare admission events flowing through an Apache Kafka pipeline.

It is the first component of a full streaming architecture that will later include:

Spark Structured Streaming

Delta Lake storage

Real‑time dashboards

*******************************************************************************

Real‑Time Pipeline Architecture


Windows Host (Python Producer)
        |
        |  PLAINTEXT_HOST://localhost:29092
        v
+---------------------+
|   Kafka Broker      |
|  (Docker Container) |
+---------------------+
        ^
        |  PLAINTEXT://kafka:9092
        |
+---------------------+
|     Kafka UI        |
|  (Docker Container) |
+---------------------+


---
Components

1. Kafka Cluster (Docker)
       - Zookeeper
       - Kafka Broker
       - Dual‑listener configuration
       - Exposed ports:
            9092 (Docker internal)
            29092 (Windows host)
2. Kafka‑UI
     A browser‑based interface for inspecting:
       - Brokers
       - Topics
       - Partitions
       - Real‑time messages

3. Python Producer

  Streams 1,000 synthetic healthcare admission events into Kafka.

       - Each event includes:
       - Patient ID
       - Hospital unit
       - Vital signs
       - Primary condition
       - Admission timestamp


How to Run the Streaming Module
1. Start Kafka + Kafka‑UI
    From the /docker folder:

        docker compose up -d
2. Run the Python Producer
    From the /producer folder:
        python healthcare_producer.py
Expected output:

   Sending 1000 events to topic: healthcare_admissions_stream
   1/1000 Sent: {...}
   2/1000 Sent: {...}
...
3. View Messages in Kafka‑UI

Open:
   http://localhost:8080
   Navigate to:

   local → Topics → healthcare_admissions_stream → Messages
##  📁 Folder Structure

cloud_streaming_healthcare/
│
├── docker/
│   └── docker-compose.yml
├── producer/
│   └── healthcare_producer.py
├── consumer/
├── etl/
│   └── generate_healthcare_data.py
├── data_raw/
├── data_processed/
└── README.md


=> Project Status
Component	               Status
Batch ETL pipeline	       Completed
Kafka cluster	               Running
Kafka‑UI	                       Connected
Python producer	               Streaming 1000 events
Spark Structured Streaming     Next step
Delta Lake storage	       Planned
Real‑time dashboard	       Planned


```






