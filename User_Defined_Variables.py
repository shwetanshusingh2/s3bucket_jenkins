import boto3
import User_Defined_Variables as user_variable



s3_client = boto3.resource('s3')
SOURCE_BUCKET = "data-shwet"
TEMPLATE_NAME = "template.yaml"

STACK_NAME = "stack234"

CLIENT = boto3.client('cloudformation')
UPLOAD_OBJECT_BUCKET = "shwet23"
TEMPLATE_URL = 'https://data-shwet.s3.ap-south-1.amazonaws.com/template.yaml'

S3_OUTPUT = 's3://shwet2/output'

