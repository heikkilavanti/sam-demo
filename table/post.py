if __name__ != "table.post":
    from lib.db import Db
else:
    from .lib.db import Db


def handler(event, context):
    database = Db()
    response = database.create_table()
    if response:
        return {
            "statusCode": 201,
        }
    return {
        "statusCode": 403,
    }
