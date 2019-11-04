import json
import boto3
import os
s3 = boto3.resource('s3')
def handler(event, context):
    bucket = s3.Bucket(os.environ['source'])
    dest_bucket = s3.Bucket(os.environ['des'])
    key = event['Records'][0]['s3']['object']['key']
    for obj in bucket.objects.all():
        if (obj.key == key):
            dest_key = obj.key
            print(obj.key)
            s3.Object(dest_bucket.name, dest_key).copy_from(CopySource={'Bucket': obj.bucket_name, 'Key': obj.key})