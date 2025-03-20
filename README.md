# INFO-I-535-Big-Data-Project
Air Quality Analysis Using Big Data

Project Overview

This project aims to analyze global air quality trends by leveraging big data technologies and advanced analytical methods. The dataset used records air quality levels across various countries and includes detailed pollutant information such as CO, Ozone, NO2, and PM2.5.

Features

Data Preprocessing: Cleaned and structured dataset using Python (Pandas, NumPy) in Google Colab.

Cloud Integration: Stored dataset in Google Cloud Platform (GCP) for secure and scalable data processing.

BigQuery Analysis: Conducted SQL-based queries to derive insights.

Data Visualization: Created interactive dashboards using Looker Studio.

Air Quality Trends: Analyzed AQI values, pollutant contributions, and regional air quality patterns.

Technologies Used

Google Cloud Platform (GCP): For data storage and querying.

Google Colab: For data preprocessing.

BigQuery: For executing SQL queries.

Looker Studio: For visualization.

Python: Pandas, Matplotlib, Seaborn for analysis.

Dataset

The dataset used in this project contains:

16,695 records

Geographical data (Country, City, Coordinates)

Pollutant levels (CO, Ozone, NO2, PM2.5)

Air Quality Index (AQI) values

Data Pipeline

Plan: Set objectives to analyze global air quality trends.

Obtain: Collected air quality data from Kaggle.

Assure: Performed data cleaning, handling missing values, and removing outliers.

Transform: Preprocessed the data in Python and uploaded it to GCP.

Store: Saved the cleaned dataset in a GCP bucket.

Analyze: Used BigQuery to conduct SQL-based analysis.

Visualize: Created dashboards using Looker Studio.

Publish: Shared the dataset and scripts on GitHub.

Analysis & Key Findings

Highest AQI Countries: Countries like Mauritania, Saudi Arabia, and Gambia recorded the highest AQI values.

Pollutant Contribution: PM2.5 is the dominant pollutant affecting AQI levels.

Geographical Trends: Northern Hemisphere has higher AQI values compared to the Southern Hemisphere.

Best & Worst Cities: Identified cities with the best and worst air quality levels.

Challenges Faced

Setting up Google Cloud Dataproc for PySpark

BigQuery integration issues due to schema mismatches

Looker Studio limitations in handling complex visualizations

Time constraints in debugging technical issues

Repository Structure

How to Run the Project

Clone the repository:

Open preprocessing.ipynb in Google Colab and run the preprocessing steps.

Upload cleaned data to Google Cloud Storage.

Import data into BigQuery and execute queries in aqi_analysis.sql.

View visualizations in Looker Studio using the shared report.

Contributors

Satya Priyanka Ponduru - Graduate Student at Indiana University BloomingtonEmail: sponduru@iu.edu

