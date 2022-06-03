import boto3
from boto3.dynamodb.conditions import Key, Attr

re = boto3.resource('dynamodb')
table = re.Table('Customers')

response1 = table.query(
    KeyConditionExpression=Key('PK').eq('CUSTOMER#Sara')
)
print("response1: \n", response1['Items'])

response2 = table.query(
    KeyConditionExpression=Key('PK').eq('CUSTOMER#the_don') & Key('SK').lt('C')
)
print("response2: \n", response2['Items'])

response3 = table.query(
    IndexName="ItemIdIndex",
    KeyConditionExpression=Key('ItemId').eq('48d7')
)
print("response3: \n", response3['Items'])

response4 = table.scan(
    FilterExpression=Attr('Email address').eq('sara@gmail.com')
)
print("response4: \n", response4['Items'])

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
