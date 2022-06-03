import boto3

re = boto3.resource('dynamodb')
table = re.Table('Customers')

res = table.put_item(
    Item={
        'PK': 'CUSTOMER#thu',
        'SK': 'CUSTOMER#thu',
        'Username': 'thu',
        'Email Address': 'thu@gmail.com',
        'Name': 'Thu',
    }
)
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "PK": 'CUSTOMER#huynh',
            "SK": 'CUSTOMER#huynh',
            "Username": 'huynh',
            "Email Address": 'huynh@gmail.com',
            "Name": 'Huynh'
        }
    )
    batch.put_item(
        Item={
            "PK": 'CUSTOMER#nguyen',
            "SK": 'CUSTOMER#nguyen',
            "Username": 'nguyen',
            "Email Address": 'nguyen@gmail.com',
            "Name": 'Nguyen'
        }
    )
res1 = table.get_item(
    Key={
        'PK': 'CUSTOMER#thu',
        'SK': 'CUSTOMER#thu'
    }
)
print(res1['Item'])