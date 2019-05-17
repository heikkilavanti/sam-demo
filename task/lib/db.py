import uuid
import os
import boto3


class Db:
    table_name = "Tasks"
    dynamo_db_url = os.environ.get("DYNAMO_DB_URL") \
        if os.environ.get("DYNAMO_DB_URL") else "http://dynamodb:8080"

    def __init__(self):
        self.db_resource = boto3.resource('dynamodb', region_name="eu-north-1")
        self.table = self.db_resource.Table(self.table_name)

    def create_task(self, task_title, task_details):
        task = Task(title=task_title, details=task_details)
        response = self.table.put_item(Item={
            "taskId": task.task_id,
            "state": task.state,
            "title": task.title,
            "details": task.details})
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return task.task_id
        return None

    def get_all_tasks(self):
        try:
            return self.table.scan()['Items']
        except:
            return None

    def delete_task(self, task_id):
        task = Task(task_id=task_id)
        print(task)
        return self.table.delete_item(Key={
            "taskId": task.task_id, "state": task.state})


class Task:

    def __init__(self, task_id=uuid.uuid4().hex, title="", details="Jahuu"):
        self.task_id = task_id
        self.state = "CREATED"
        self.title = title
        self.details = details