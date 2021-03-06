# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import builtins
import typing
import os

import aws_cdk as cdk
from constructs import Construct

# from api.infrastructure import API
# from database.infrastructure import Database
from datalake.infrastructure import DataLake
from etl.infrastructure import ETLJob


# class UserManagementBackend(cdk.Stage):
#     def __init__(
#         self,
#         scope: Construct,
#         id_: str,
#         *,
#         database_dynamodb_billing_mode: dynamodb.BillingMode,
#         api_lambda_reserved_concurrency: int,
#         **kwargs: Any,
#     ):
#         super().__init__(scope, id_, **kwargs)

#         stateful = cdk.Stack(self, "Stateful")
#         database = Database(
#             stateful, "Database", dynamodb_billing_mode=database_dynamodb_billing_mode
#         )
#         stateless = cdk.Stack(self, "Stateless")
#         api = API(
#             stateless,
#             "API",
#             dynamodb_table=database.table,
#             lambda_reserved_concurrency=api_lambda_reserved_concurrency,
#         )
#         # Monitoring(stateless, "Monitoring", database=database, api=api)

#         self.api_endpoint_url = api.endpoint_url


class AnalyticsPipeline(cdk.Stage):
    def __init__(
        self,
        scope: Construct,
        id_: builtins.str,
        *,
        env: typing.Optional[cdk.Environment] = None,
        outdir: typing.Optional[builtins.str] = None
    ) -> None:
        super().__init__(scope, id_, env=env, outdir=outdir)

        stateful = cdk.Stack(self, "Stateful")
        datalake = DataLake(stateful, "DataLake")

        stateless = cdk.Stack(self, "Stateless")

        script = os.path.join(os.getcwd(), "job-scripts/transform.py")
        etl = ETLJob(stateless, "ETLJob", script_path=script)
