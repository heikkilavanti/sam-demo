import boto3
import uuid



class Db(object):

    table_name = "Tasks"

    def __init__(self):
        self.db_client = boto3.client('dynamodb', region_name="eu-north-1")

    def create_table(self):
        existing_tables = self.db_client.list_tables()['TableNames']
        if self.table_name not in existing_tables:
            return self.db_client.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': 'taskId',
                        'AttributeType': 'S',
                    },
                    {
                        'AttributeName': 'state',
                        'AttributeType': 'S',
                    },
                ],
                KeySchema=[
                    {
                        'AttributeName': 'taskId',
                        'KeyType': 'HASH',
                    },
                    {
                        'AttributeName': 'state',
                        'KeyType': 'RANGE',
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5,
                },
                TableName=self.table_name,
            )
        else:
            return "OK"

    def delete_table(self):
        existing_tables = self.db_client.list_tables()['TableNames']
        if self.table_name in existing_tables:
            return self.db_client.delete_table(TableName=self.table_name)
