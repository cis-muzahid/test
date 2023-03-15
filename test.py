import os

try:
    password = os.environ['DB_PASSWORD']
    S3_BUCKET = os.environ['AWS_S3_BUCKET']
except Exception as err:
    raise Exception(err)
