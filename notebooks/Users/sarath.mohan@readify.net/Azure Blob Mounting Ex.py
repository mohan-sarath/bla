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

df1000.createOrReplaceTempView("myview1000")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count (*) from myview1000

# COMMAND ----------

df1_5mil = spark.read.text("/mnt/testmount/1500000 Sales Records.csv")

# COMMAND ----------

df1_5mil.createOrReplaceTempView("myview1_5mil")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count (*) from myview1_5mil

# COMMAND ----------

