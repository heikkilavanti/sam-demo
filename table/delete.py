if __name__ != "table.delete":
    from lib.db import Db
else:
    from .lib.db import Db


def handler(event, context):
    print(event)
    database = Db()
    response = database.delete_table()
    print(response)
    if response:
        return {
            "statusCode": 204,
        }
    else:
        return {
            "statusCode": 403,
        }