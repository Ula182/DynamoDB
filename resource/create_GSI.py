import boto3

# query, put_item, scan

re = boto3.client('dynamodb')
try:
    resp = re.update_table(
        TableName="Customers",
        AttributeDefinitions=[
            {
                "AttributeName": "Addresses",
                "AttributeType": "S"
            },
        ],
       
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    
                    "IndexName": "AddressesIndex",
                 
                    "KeySchema": [
                        {
                            "AttributeName": "Addresses",
                            "KeyType": "HASH"
                        }
                    ],
                    
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1,
                    }
                }
            }
        ],
    )
    print("Secondary index added!")
except Exception as e:
    print("Error updating table:")
    print(e)

# try:
#     resp = re.update_table(
#         TableName="Customers",
#         AttributeDefinitions=[
#             {
#                 "AttributeName": "ItemId",
#                 "AttributeType": "S"
#             },
#         ],
       
#         GlobalSecondaryIndexUpdates=[
#             {
#                 "Create": {
                    
#                     "IndexName": "ItemIdIndex",
                 
#                     "KeySchema": [
#                         {
#                             "AttributeName": "ItemId",
#                             "KeyType": "HASH"
#                         }
#                     ],
                    
#                     "Projection": {
#                         "ProjectionType": "ALL"
#                     },
                    
#                     "ProvisionedThroughput": {
#                         "ReadCapacityUnits": 1,
#                         "WriteCapacityUnits": 1,
#                     }
#                 }
#             }
#         ],
#     )
#     print("Secondary index added!")
# except Exception as e:
#     print("Error updating table:")
#     print(e)
