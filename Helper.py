import boto3
from botocore.client import ClientError
import os

os.environ['AWS_SHARED_CREDENTIALS_FILE'] = "C:/Users/Hp/.aws/credentials"

os.environ['AWS_PROFILE'] = "default"
os.environ['AWS_DEFAULT_REGION'] = "ap-south-1"

import User_Defined_Variables as user_variable
import zipfile,os
import time
import stack as s
s3 = boto3.resource('s3')



try:
    s3.create_bucket(Bucket='data-shwet', CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
except ClientError:
    print("Data Bucket Already Created")
s3.Object('data-shwet', 'template.yaml').upload_file(Filename='template.yaml')
locfile = "lambda_function1.py"
loczip = "lambda_function1.zip"
zip = zipfile.ZipFile (loczip, "w")
zip.write (locfile,os.path.basename(locfile))
zip.close()
s3.Object('data-shwet', 'lambda_function1.zip').upload_file(Filename='lambda_function1.zip')
os.remove("lambda_function1.zip")
client = boto3.client('cloudformation')
stack = s.stack()
stack.create_upload_stack()



