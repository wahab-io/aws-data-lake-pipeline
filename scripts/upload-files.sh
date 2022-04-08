#!/bin/bash

aws s3 cp data/SalesOrders.csv_split_aa s3://analyticspipelinesandbox-datalakesalesbucketb2cbb-ld7z7cq9d2x0/raw-data/
aws s3 cp data/SalesOrders.csv_split_ab s3://analyticspipelinesandbox-datalakesalesbucketb2cbb-ld7z7cq9d2x0/raw-data/
