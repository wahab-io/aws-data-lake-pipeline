import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)
## @type: DataSource
## @args: [database = "salesdb", table_name = "raw_data", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="sales-db", table_name="raw-sales-records", transformation_ctx="datasource0"
)
## @type: ApplyMapping
## @args: [mapping = [("﻿row id", "long", "﻿row id", "long"), ("order id", "string", "order id", "string"), ("order date", "string", "order date", "string"), ("ship date", "string", "ship date", "string"), ("ship mode", "string", "ship mode", "string"), ("customer id", "string", "customer id", "string"), ("customer name", "string", "customer name", "string"), ("segment", "string", "segment", "string"), ("city", "string", "city", "string"), ("state", "string", "state", "string"), ("country", "string", "country", "string"), ("postal code", "long", "postal code", "long"), ("market", "string", "market", "string"), ("region", "string", "region", "string"), ("product id", "string", "product id", "string"), ("category", "string", "category", "string"), ("sub-category", "string", "sub-category", "string"), ("product name", "string", "product name", "string"), ("sales", "double", "sales", "double"), ("quantity", "long", "quantity", "long"), ("discount", "double", "discount", "double"), ("profit", "double", "profit", "double"), ("shipping cost", "double", "shipping cost", "double"), ("order priority", "string", "order priority", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(
    frame=datasource0,
    mappings=[
        ("row id", "long", "row id", "long"),
        ("order id", "string", "order id", "string"),
        ("order date", "string", "order date", "string"),
        ("ship date", "string", "ship date", "string"),
        ("ship mode", "string", "ship mode", "string"),
        ("customer id", "string", "customer id", "string"),
        ("customer name", "string", "customer name", "string"),
        ("segment", "string", "segment", "string"),
        ("city", "string", "city", "string"),
        ("state", "string", "state", "string"),
        ("country", "string", "country", "string"),
        ("postal code", "long", "postal code", "long"),
        ("market", "string", "market", "string"),
        ("region", "string", "region", "string"),
        ("product id", "string", "product id", "string"),
        ("category", "string", "category", "string"),
        ("sub-category", "string", "sub-category", "string"),
        ("product name", "string", "product name", "string"),
        ("sales", "double", "sales", "double"),
        ("quantity", "long", "quantity", "long"),
        ("discount", "double", "discount", "double"),
        ("profit", "double", "profit", "double"),
        ("shipping cost", "double", "shipping cost", "double"),
        ("order priority", "string", "order priority", "string"),
    ],
    transformation_ctx="applymapping1",
)
## @type: SelectFields
## @args: [paths = ["row id", "order id", "order date", "ship date", "ship mode", "customer id", "customer name", "segment", "city", "state", "country", "postal code", "market", "region", "product id", "category", "sub-category", "product name", "sales", "quantity", "discount", "profit", "shipping cost", "order priority"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]
selectfields2 = SelectFields.apply(
    frame=applymapping1,
    paths=[
        "row id",
        "order id",
        "order date",
        "ship date",
        "ship mode",
        "customer id",
        "customer name",
        "segment",
        "city",
        "state",
        "country",
        "postal code",
        "market",
        "region",
        "product id",
        "category",
        "sub-category",
        "product name",
        "sales",
        "quantity",
        "discount",
        "profit",
        "shipping cost",
        "order priority",
    ],
    transformation_ctx="selectfields2",
)
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "salesdb", table_name = "raw_data", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
resolvechoice3 = ResolveChoice.apply(
    frame=selectfields2,
    choice="MATCH_CATALOG",
    database="sales-db",
    table_name="raw_data",
    transformation_ctx="resolvechoice3",
)
## @type: DataSink
## @args: [database = "salesdb", table_name = "raw_data", transformation_ctx = "datasink4"]
## @return: datasink4
## @inputs: [frame = resolvechoice3]
datasink4 = glueContext.write_dynamic_frame.from_catalog(
    frame=resolvechoice3,
    database="sales-db",
    table_name="processed-sales-records",
    transformation_ctx="datasink4",
)
job.commit()
