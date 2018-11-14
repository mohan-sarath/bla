-- Databricks notebook source
-- MAGIC %python
-- MAGIC 
-- MAGIC databricks secrets put --scope <scope-name> --key <key-name>

-- COMMAND ----------

databricks secrets list --scope jdbc

-- COMMAND ----------

-- MAGIC %python
-- MAGIC 
-- MAGIC dbutils.fs.mount(
-- MAGIC   source = "wasbs://data-bricks-test@azurestorageccount2018.blob.core.windows.net/",
-- MAGIC   mount_point = "/mnt/mountsource",
-- MAGIC   extra_configs = {"fs.azure.sas.data-bricks-test.azurestorageccount2018.blob.core.windows.net":dbutils.secrets.get(scope = "<scope-name>", key = "<key-name>")})