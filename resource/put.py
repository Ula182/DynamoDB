import boto3
from boto3.dynamodb.conditions import Key, Attr

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
res1 = table.get_item(
    Key={
        'PK': 'CUSTOMER#thu',
        'SK': 'CUSTOMER#thu'
    }
)
print(res1['Item'])

res2 = table.scan(
    FilterExpression=Attr('Addresses').exists()
)
print("res2: \n", res2.get('Items', 'b')[0])

res3 = table.update_item(
    Key={'PK': 'CUSTOMER#thu', 'SK': 'CUSTOMER#thu'},
    ExpressionAttributeNames={
        "#name": "Name",
    },
    ExpressionAttributeValues={
        ':n': 'thuuyen'
    },
    UpdateExpression="SET #name = :n",

)
print(res3)

res4 = table.delete_item(
    Key={
        'PK': 'CUSTOMER#Sara',
        'SK': 'CUSTOMER#Sara'
    }
)
print(res4)

res5 = table.query(
    KeyConditionExpression=Key('PK').eq('CUSTOMER#thu')
)
print("res5: \n", res5['Items'])
