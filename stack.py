import boto3
from botocore.client import ClientError
import User_Defined_Variables as user_variable
import zipfile,os
import time

class stack:

    def stack_status(self, stack_name):
            try:
                stack = user_variable.CLIENT.describe_stacks(StackName=stack_name)
                status = stack['Stacks'][0]['StackStatus']
                return status
            except Exception:
                return "NO_STACK"

        # checks whether the update or create stack is required based on the present status of the stack

    def create_upload_stack(self):


            status = self.stack_status(user_variable.STACK_NAME)
            if status == 'ROLLBACK_COMPLETE' or \
                    status == 'ROLLBACK_FAILED' or \
                    status == 'UPDATE_ROLLBACK_COMPLETE' or \
                    status == 'DELETE_FAILED':

                self.delete_object('shwet231')
                self.delete_object('shwet231-des')
                user_variable.CLIENT.delete_stack(StackName=user_variable.STACK_NAME)
                while self.stack_status(user_variable.STACK_NAME) == 'DELETE_IN_PROGRESS':
                    time.sleep(1)
                print("stack deleted")
                self.create_stack(user_variable.STACK_NAME, user_variable.TEMPLATE_URL,
                                  )
                print("stack initialising")

            elif status == 'CREATE_COMPLETE' or status == 'UPDATE_COMPLETE':
                self.update_stack(user_variable.STACK_NAME, user_variable.TEMPLATE_URL)
                print("stack updated")
            else:
                self.create_stack(user_variable.STACK_NAME, user_variable.TEMPLATE_URL)
                print("stack initialising")

            while self.stack_status(user_variable.STACK_NAME) == 'CREATE_IN_PROGRESS' or \
                    self.stack_status(user_variable.STACK_NAME) == 'UPDATE_IN_PROGRESS' or \
                    self.stack_status(user_variable.STACK_NAME) == 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS':
                print("waiting for creation or deletion")
                time.sleep(1)
            print("stack created")

    def delete_object(self, bucket_name):
            try:
                bucket = user_variable.s3_client.Bucket(bucket_name)
                bucket.objects.all().delete()
            except Exception:
                print("Bucket Not Present")

    def create_stack(self, stack_name, template_url):
            response = user_variable.CLIENT.create_stack(
                StackName=stack_name,
                TemplateURL=template_url,
                Capabilities=['CAPABILITY_NAMED_IAM']

            )

    def update_stack(self, stack_name, template_url):
            try:
                response = user_variable.CLIENT.update_stack(
                    StackName=stack_name,
                    TemplateURL=template_url,
                    Capabilities=['CAPABILITY_NAMED_IAM']

                )
            except Exception:
                print("No update To Perform")
