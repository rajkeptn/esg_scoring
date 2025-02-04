from pyspark.sql.functions import udf
from pyspark.sql.types import *
 
with_topics_schema = ArrayType(StructType([
    StructField("id", IntegerType(), False),
    StructField("probability", FloatType(), False)
]))
 
@udf(with_topics_schema)
def with_topic(ps):
  return [[i, p] for i, p in enumerate(ps)]