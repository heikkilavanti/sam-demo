if __name__ != "table.delete":
    from lib.db import Db
else:
    from .lib.db import Db


def handler(event, context):
    database = Db()
    response = database.delete_table()
    if response:
        return {
            "statusCode": 204,
        }
    return {"statusCode": 403, }
