import json
import ast

if __name__ != "task.post":
    from lib.db import Db
else:
    from .lib.db import Db


def handler(event, context):
    db = Db()
    print(event)
    task_title = ast.literal_eval(event.get('body')).get('taskTitle')
    task_details = ast.literal_eval(event.get('body')).get('taskDetails')
    if task_title:
        response = db.create_task(task_title, task_details)
        if response:
            return {
                "statusCode": 201,
                "body": json.dumps({
                    "taskId": response
                 })
            }
        return {
            "statusCode": 500,
            "message": "Error while saving to database"
        }
    return {
        "statusCode": 400,
        "body": json.dumps({
            "error": "taskTitle and taskDetails must be given"
        })
    }
