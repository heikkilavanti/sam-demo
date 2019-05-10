import json


if __name__ != "task.delete":
    from lib.db import Db
else:
    from .lib.db import Db


def handler(event, context):
    db = Db()
    print(event)
    task_id = event.get('pathParameters').get('id')
    print(id)
    if task_id:
        response = db.delete_task(task_id)
        print(response)
        return {
            "statusCode": 204,
        }
    return {
        "statusCode": 400,
        "body": json.dumps({
            "error": "id must be given"
        })
    }