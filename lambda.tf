provider "aws" {
  region = "eu-central-1"
}

resource "aws_s3_bucket" "bucket" {
  bucket = "sjones-s3-bucket-coin-changer-2"
}

resource "aws_lambda_function" "coin-changer-2" {
  function_name = "CoinChanger2"

  s3_bucket = "sjones-s3-bucket-coin-changer-2"
  s3_key = "lambda.zip"

  handler = "changer.handler"
  runtime = "python3.6"

  role = "${aws_iam_role.lambda_exec.arn}"
}

resource "aws_iam_role" "lambda_exec" {
  name = "sjones-coin-changer-2-lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_permission" "apigw" {
  statement_id = "AllowAPIGatewayInvoke"
  action = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.coin-changer-2.function_name}"
  principal = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.coin-changer-2-api.execution_arn}/*/*"
}
