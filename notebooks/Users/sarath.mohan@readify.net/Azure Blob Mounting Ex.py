# Databricks notebook source
dbutils.fs.mount(
  source = "wasbs://data-bricks-test@azurestorageccount2018.blob.core.windows.net/",
  mount_point = "/mnt/testmount",
  extra_configs = {"fs.azure.account.key.azurestorageccount2018.blob.core.windows.net":dbutils.secrets.get(scope = "azureblob", key = "blobstore")})



# COMMAND ----------

dbutils.fs.unmount("/mnt/testmount")

# COMMAND ----------

df1000 = spark.read.text("/mnt/testmount/10000 Sales Records.csv")

# COMMAND ----------

display(df1000.select("*"))

# COMMAND ----------

df1000 = spark.read.text("/mnt/testmount/10000 Sales Records.csv")