import boto3

# Get the service resource.
dynamodb = boto3.client('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Customers',
    KeySchema=[
        {
            'AttributeName': 'PK',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'SK',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'PK',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'SK',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
# table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)
