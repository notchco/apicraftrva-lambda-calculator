import time
from datetime import datetime
import boto3
DDB = boto3.resource('dynamodb').Table('calculations')


def handler(event, context):
    a = int(event['a'])
    b = int(event['b'])
    op = event['op']
    c = None

    if op == '+' or op == 'add':
        c = a + b
    elif op == '-' or op == 'subtract':
        c = a - b
    elif op == '*' or op == 'multiply':
        c = a * b
    elif op == '/' or op == 'divide':
        c = a / b
    else:
        return "operation not allowed"

    res = {'a': a, 'b': b, 'op': op, 'c': c}

    now = datetime.utcnow()
    timestamp = int(time.mktime(now.timetuple()))
    res['timestamp'] = str(timestamp)

    item = {'Item': res}

    DDB.put_item(**item)

    return res
