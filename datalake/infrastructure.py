import builtins

from constructs import Construct

from aws_cdk import aws_s3 as s3
from aws_cdk import aws_glue_alpha as glue
from aws_cdk import aws_glue as glue_cfn


class DataLake(Construct):
    def __init__(self, scope: Construct, id_: builtins.str) -> None:
        super().__init__(scope, id_)

        sales_lake = s3.Bucket(self, "SalesBucket")

        sales_db = glue.Database(self, "SalesDatabase", database_name="sales-db")

        glue.Table(
            self,
            "SalesTable",
            columns=[
                glue.Column(name="Row Id", type=glue.Schema.BIG_INT),
                glue.Column(name="Order Id", type=glue.Schema.STRING),
                glue.Column(name="Order Date", type=glue.Schema.STRING),
                glue.Column(name="Ship Date", type=glue.Schema.STRING),
                glue.Column(name="Ship Mode", type=glue.Schema.STRING),
                glue.Column(name="Customer Id", type=glue.Schema.STRING),
                glue.Column(name="Customer Name", type=glue.Schema.STRING),
                glue.Column(name="Segment", type=glue.Schema.STRING),
                glue.Column(name="City", type=glue.Schema.STRING),
                glue.Column(name="State", type=glue.Schema.STRING),
                glue.Column(name="Country", type=glue.Schema.STRING),
                glue.Column(name="Postal Code", type=glue.Schema.BIG_INT),
                glue.Column(name="Market", type=glue.Schema.STRING),
                glue.Column(name="Region", type=glue.Schema.STRING),
                glue.Column(name="Product Id", type=glue.Schema.STRING),
                glue.Column(name="Category", type=glue.Schema.STRING),
                glue.Column(name="Sub-Category", type=glue.Schema.STRING),
                glue.Column(name="Product Name", type=glue.Schema.STRING),
                glue.Column(name="Sales", type=glue.Schema.DOUBLE),
                glue.Column(name="Quantity", type=glue.Schema.BIG_INT),
                glue.Column(name="Discount", type=glue.Schema.DOUBLE),
                glue.Column(name="Profit", type=glue.Schema.DOUBLE),
                glue.Column(name="Shipping Cost", type=glue.Schema.DOUBLE),
                glue.Column(name="Order Priority", type=glue.Schema.STRING),
            ],
            database=sales_db,
            data_format=glue.DataFormat.CSV,
            table_name="sales-records",
            bucket=sales_lake,
            s3_prefix="raw-data",
        )
