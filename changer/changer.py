import json

def handler(event, context):
    change_amount = event['queryStringParameters']['change_amount']
    response = {
        'statusCode': 200,
        'body': json.dumps(calculate(change_amount))
    }
    return response

def calculate(change_amount, coins=None):
    if coins is None: coins = []
    for coin in (200, 100, 50, 20, 10, 5, 2, 1):
        if change_amount >= coin:
            for _ in range(int(change_amount / coin)):
                change_amount -= coin
                coins.append(coin)
    return coins
