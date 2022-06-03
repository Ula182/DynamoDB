import boto3

client = boto3.client('dynamodb')
response = client.transact_write_items(
    TransactItems=[
        {
            'Put': {
                'TableName': 'Customers',
                'Item': {
                    'PK': {'S': 'CUSTOMER#alexdebrie'},
                    'SK': {'S': 'CUSTOMER#alexdebrie'},
                    'Username': {'S': 'alexdebrie'},
                    'Email Address': {'S': 'alexdebrie1@gmail.com'},
                    'Name': {'S': 'Alex DeBrie'},
                    'Addresses': {
                        'M': {
                            "Home": {
                                'M': {
                                    "Street": {"S": "112 1st Street"}, 
                                    "City": {"S": "Omaha"}, 
                                    "State": {"S": "NE"}
                                }
                            },
                            "Business": {
                                "M": {
                                    "Street": {"S": "555 Broadway"}, 
                                    "City": {"S": "Omaha"}, 
                                    "State": {"S": "NE"}
                                }
                            }
                        },
                    },
                },
                'ConditionExpression': 'attribute_not_exists(SK)',
            }
        },
        {
            'Put': {
                'TableName': 'Customers',
                'Item': {
                    'PK': {'S': 'CUSTOMER#the_don'},
                    'SK': {'S': 'CUSTOMER#the_don'},
                    'Username': {'S': 'the_don'},
                    'Email Address': {'S': 'vito@corleone.com'},
                    'Name': {'S': 'vito Coleone'},
                    'Addresses': {
                        'M': {
                            "Home": {
                                'M':
                                {
                                    "Street": {"S": "987 Fifth Avenue"},
                                    "City": {"S": "New York"},
                                    "State": {"S": "NY"}
                                }
                            },
                        },
                    },
                },
                'ConditionExpression': 'attribute_not_exists(SK)'
            }
        },
        {
            'Put': {
                'TableName': 'Customers',
                'Item': {
                    'PK': {'S': 'CUSTOMER#alexdebrie'},
                    'SK': {'S': '#ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY'},
                    'Orderld': {'S': '1VrgXBQ0VCshuQUnh1HrDIHQNwY'},
                    'CreatedAt': {'S': '2020-01-03 01:57:44'},
                    'Status': {'S': 'SHIPPED'},
                    'Amount': {'N': '67.43'},
                    'NumberItems': {'N': '7'},
                    'GSI1PK': {'S': 'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY'},
                    'GSI1SK': {'S': 'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY'}
                },
                'ConditionExpression': 'attribute_not_exists(SK)',
            }
        },
        {
            'Put': {
                'TableName': 'Customers',
                'Item': {
                    'PK': {'S': 'CUSTOMER#alexdebrie'},
                    'SK': {'S': '#ORDER#1VwVAvJk1GvBFfpTAjm0KG7Cg9d'},
                    'Orderld': {'S': '1VwVAvJk1GvBFfpTAjm0KG7Cg9d'},
                    'CreatedAt': {'S': '2020-01-04 18:53:24'},
                    'Status': {'S': 'CANCELLED'},
                    'Amount': {'N': '12.43'},
                    'NumberItems': {'N': '2'},
                    'GSI1PK': {'S': 'ORDER#1VwVAvJk1GvBFfpTAjm0KG7Cg9d'},
                    'GSI1SK': {'S': 'ORDER#1VwVAvJk1GvBFfpTAjm0KG7Cg9d'}
                },
                'ConditionExpression': 'attribute_not_exists(SK)',
            }
        },
        {
            'Put': {
                'TableName': 'Customers',
                'Item': {
                    'PK': {'S': 'CUSTOMER#the_don'},
                    'SK': {'S': '#ORDER#1W1hwN4ywvTR6xzwhU8EHbXULBa'},
                    'Orderld': {'S': '1W1hwN4ywvTR6xzwhU8EHbXULBa'},
                    'CreatedAt': {'S': '2020-01-06 18:53:24'},
                    'Status': {'S': 'DELIVERED'},
                    'Amount': {'N': '98.54'},
                    'NumberItems': {'N': '4'},
                    'GSI1PK': {'S': 'ORDER#1W1hwN4ywvTR6xzwhU8EHbXULBa'},
                    'GSI1SK': {'S': 'ORDER#1W1hwN4ywvTR6xzwhU8EHbXULBa'}
                },
                'ConditionExpression': 'attribute_not_exists(SK)'
            }
        },
        {
            'Put': {
                'TableName': 'Customers',
                'Item': {
                    'PK': {'S': 'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY#ITEM#48d7'},
                    'SK': {'S': 'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY#ITEM#48d7'},
                    'Orderld': {'S': '88da49e72b80'},
                    'ItemId': {'S': '48d7'},
                    'Description': {'S': 'Go, Dog, Go!'},
                    'Price': {'N': '9.72'},
                    'GSI1PK': {'S': 'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY'},
                    'GSI1SK': {'S': 'ITEM#48d7'}
                },
                'ConditionExpression': 'attribute_not_exists(SK)',
            }
        },
        {
            'Put': {
                'TableName': 'Customers',
                'Item': {
                    'PK': {'S': 'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY#TEM#be43'},
                    'SK': {'S': 'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY#TEM#be43'},
                    'Orderld': {'S': '88da49e72b80'},
                    'ItemID': {'S': 'be43'},
                    'Status': {'S': 'CANCELLED'},
                    'Description': {'S': 'Les Miserables'},
                    'Price': {'N': '14.64'},
                    'GSI1PK': {'S': 'ORDER#1VrgXBQ0VCshuQUnh1HrDIHQNwY'},
                    'GSI1SK': {'S': 'ITEM#be43'}
                },
                'ConditionExpression': 'attribute_not_exists(SK)'
            }
        }
    ]
)
