import sys
import json

import changer.changer as changer


def cli_main() -> None:
    if __invalid_args():
        raise Exception('Please provide a numeric argument')
    else:
        print(changer.change(int(sys.argv[1])))


def __invalid_args() -> bool:
    return len(sys.argv) < 2 or sys.argv[1].isdigit() is False


def lambda_main(event, context) -> dict:
    change_amount = int(event['queryStringParameters']['change_amount'])
    response = {
        'statusCode': 200,
        'body': json.dumps(changer.change(change_amount))
    }
    return response


if __name__ == '__main__': cli_main()