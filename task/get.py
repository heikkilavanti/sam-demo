import json


if __name__ != "task.get":
    from lib.db import Db
else:
    from .lib.db import Db


def handler(event, context):
    db = Db()

    response = db.get_all_tasks()
    if response:
        return {
            "statusCode": 200,
            "body": json.dumps(response),
        }
    else:
        return {
            "statusCode": 404,
        }
