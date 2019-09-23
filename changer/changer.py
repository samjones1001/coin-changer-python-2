import json


def handler(event, context):
    change_amount = int(event['queryStringParameters']['change_amount'])
    response = {
        'statusCode': 200,
        'body': json.dumps(calculate(change_amount))
    }
    return response


def calculate(change_amount, denominations=(200, 100, 50, 20, 10, 5, 2, 1)):
    coins = []
    for coin in denominations:
        while change_amount >= coin:
            change_amount -= coin
            coins.append(coin)
    return coins


