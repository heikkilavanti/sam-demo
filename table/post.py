if __name__ != "table.post":
    from lib.db import Db
else:
    from .lib.db import Db


def handler(event, context):
    print(f"My name is {__name__}")
    print(event)
    database = Db()
    response = database.create_table()
    print(response)
    if response:
        return {
            "statusCode": 204,
        }
    else:
        return {
            "statusCode": 403,
        }
