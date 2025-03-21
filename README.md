# Air Quality Analysis Using Big Data

### Project Overview
This project aims to analyze global air quality trends by leveraging big data technologies and advanced analytical methods. The dataset used records air quality levels across various countries and includes detailed pollutant information such as CO, Ozone, NO2, and PM2.5.

### Features
1. Data Preprocessing: Cleaned and structured dataset using Python (Pandas, NumPy) in Google Colab.
2. Cloud Integration: Stored dataset in Google Cloud Platform (GCP) for secure and scalable data processing.
3. BigQuery Analysis: Conducted SQL-based queries to derive insights.
4. Data Visualization: Created interactive dashboards using Looker Studio.
5. Air Quality Trends: Analyzed AQI values, pollutant contributions, and regional air quality patterns.

### Technologies Used
1. Google Cloud Platform (GCP): For data storage and querying.
2. Google Colab: For data preprocessing.
3. BigQuery: For executing SQL queries.
4. Looker Studio: For visualization.
5. Python: Pandas, Matplotlib, Seaborn for analysis.

### Dataset
The dataset used in this project contains:
1. 16,695 records
2. Geographical data (Country, City, Coordinates)
3. Pollutant levels (CO, Ozone, NO2, PM2.5)
4. Air Quality Index (AQI) values

### Data Pipeline
1. Plan: Set objectives to analyze global air quality trends.
2. Obtain: Collected air quality data from Kaggle.
3. Assure: Performed data cleaning, handling missing values, and removing outliers.
4. Transform: Preprocessed the data in Python and uploaded it to GCP.
5. Store: Saved the cleaned dataset in a GCP bucket.
6. Analyze: Used BigQuery to conduct SQL-based analysis.
7. Visualize: Created dashboards using Looker Studio.
8. Publish: Shared the dataset and scripts on GitHub.

### Analysis & Key Findings
1. Highest AQI Countries: Countries like Mauritania, Saudi Arabia, and Gambia recorded the highest AQI values.
2. Pollutant Contribution: PM2.5 is the dominant pollutant affecting AQI levels.
3. Geographical Trends: Northern Hemisphere has higher AQI values compared to the Southern Hemisphere.
4. Best & Worst Cities: Identified cities with the best and worst air quality levels.

### Challenges Faced
1. Setting up Google Cloud Dataproc for PySpark
2. BigQuery integration issues due to schema mismatches
3. Looker Studio limitations in handling complex visualizations
4. Time constraints in debugging technical issues

### Repository Structure

#### How to Run the Project
1. Clone the repository:
2. Open preprocessing.ipynb in Google Colab and run the preprocessing steps.
3. Upload cleaned data to Google Cloud Storage.
4. Import data into BigQuery and execute queries in aqi_analysis.sql.
5. View visualizations in Looker Studio using the shared report.
