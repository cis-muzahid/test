import os

try:
    password = os.environ['DB_PASSWORD']
except Exception as err:
    raise Exception(err)