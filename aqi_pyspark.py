from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Define Spark session with BigQuery support
spark = SparkSession.builder \
    .appName("AQI Regression Analysis") \
    .config('spark.jars.packages', 'com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.21.0') \
    .config("spark.executor.memory", "4g") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Load data from GCS bucket
df = spark.read.csv("gs://air_quality_bucket_1/cleaned_AQI_and_Lat_Long_of_Countries.csv", header=True, inferSchema=True)
df.printSchema()

# Assemble features
assembler = VectorAssembler(
    inputCols=["CO AQI Value", "Ozone AQI Value", "NO2 AQI Value", "PM2_5 AQI Value"],
    outputCol="features"
)
output = assembler.transform(df)

# Prepare data
final_data = output.select("features", "AQI Value")
train_data, test_data = final_data.randomSplit([0.8, 0.2])

# Train model
lr = LinearRegression(featuresCol='features', labelCol='AQI Value', regParam=0.01)  # Added a regParam for regularization
lr_model = lr.fit(train_data)

# Predict
predictions = lr_model.transform(test_data)

# # Convert features to string for BigQuery compatibility
# final_predictions = predictions.selectExpr(
#     "cast(features as string) as features", 
#     "`AQI Value`", 
#     "prediction as predicted_AQI_Value"
# )

# # Write to BigQuery
# final_predictions.write.format('bigquery') \
#     .option('table', 'sp24-i535-geelapro-air-quality.cleaned_dataset.CLEANED_AQI_DATASET') \
#     .option('temporaryGcsBucket', 'gs://air_quality_bucket_1/temporary-storage') \
#     .mode('append') \
#     .save()


# Define the schema explicitly
schema = StructType([
    StructField("features", StringType(), True),
    StructField("AQI Value", IntegerType(), True),
    StructField("predicted_AQI_Value", FloatType(), False)
])

# Apply the schema
final_predictions = spark.createDataFrame(predictions.rdd, schema)

# Write to BigQuery
final_predictions.write.csv('gs://air_quality_bucket_1/final_predictions.csv')


# Stop the Spark session
spark.stop()
