import json

import boto3

import uuid

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    print("Food order process started with the data...", event)
    table_name = 'FoodOrders'
    table = dynamodb.Table(table_name)
    order_id = str(uuid.uuid4())

    print("Generated OrderId: ", order_id)
    item = {
        'OrderId': order_id,
        'name': event['name'],
        'price': event['price'],
        'address': event['address']
    }

    response = table.put_item(Item=item)

    print("Order placed successfully:", response)

    return {

        'statusCode': 200,

        'body': json.dumps('Order successfully placed!')

    }