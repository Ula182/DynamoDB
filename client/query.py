import boto3

re = boto3.resource('dynamodb')
table = re.Table('Customers')
response = table.get_item(
    Key={
        'PK': 'CUSTOMER#alexdebrie',
        'SK': 'CUSTOMER#alexdebrie'
    }
)
print(response['Item'])

client = boto3.client('dynamodb')
scan = client.scan(
    TableName='Customers',
)
print('scan: \n', scan['Items'])

resp = client.query(
    TableName='Customers',
    KeyConditionExpression='#pk = :pk',
    ExpressionAttributeNames={
        '#pk': 'PK'
    },
    ExpressionAttributeValues={
        ':pk': {'S': 'CUSTOMER#alexdebrie'}
    },
    ScanIndexForward=False,
    Limit=11
)
print("Query: \n", resp)


resp1 = client.query(
    TableName='Customers',
    KeyConditionExpression="#c = :c AND #t = :s",
    ExpressionAttributeNames={
        "#c": "PK",
        "#t": "SK",
    },
    ExpressionAttributeValues={
        ":c": {"S": "CUSTOMER#Sara"},
        ":s": {"S": "CUSTOMER#Sara"}
    }
)
print("Query_dk: \n", resp1)

resp2 = client.get_item(
    TableName='Customers',
    Key={
        'PK': {'S': 'CUSTOMER#alexdebrie'},
        'SK': {'S': '#ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY'}
    }
)
print("Get_item: \n", resp2['Item']['Amount'])


resp3 = client.put_item(
    TableName='Customers',
    Item={
        'PK': {'S': 'CUSTOMER#Sara'},
        'SK': {'S': 'CUSTOMER#Sara'},
        'Username': {'S': 'sarasara'},
        'Email address': {'S': 'sara@gmail.com'},
        'Name': {'S': 'Sara Sara'},
    }
)
print(resp3)

# resp1 = client.query(
#     TableName='Customers',
#     # IndexName='GSI1',
#     KeyConditionExpression='#gsi1pk = :gsi1pk',
#     ExpressionAttributeNames={
#         '#gsi1pk': 'GSI1PK'
#     },
#     ExpressionAttributeValues={
#         ':gsi1pk': {'S':'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY'}
#     }
# )
# print(resp1)