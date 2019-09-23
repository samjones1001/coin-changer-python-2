resource "aws_api_gateway_rest_api" "coin-changer-2-api" {
  name        = "CoinChanger2"
  description = "Coin Changer 2 API"
}

resource "aws_api_gateway_resource" "changer" {
  rest_api_id = "${aws_api_gateway_rest_api.coin-changer-2-api.id}"
  parent_id   = "${aws_api_gateway_rest_api.coin-changer-2-api.root_resource_id}"
  path_part   = "changer"
}

resource "aws_api_gateway_method" "changer" {
  rest_api_id   = "${aws_api_gateway_rest_api.coin-changer-2-api.id}"
  resource_id   = "${aws_api_gateway_resource.changer.id}"
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "changer" {
  rest_api_id             = "${aws_api_gateway_rest_api.coin-changer-2-api.id}"
  resource_id             = "${aws_api_gateway_resource.changer.id}"
  http_method             = "${aws_api_gateway_method.changer.http_method}"
  type                    = "AWS_PROXY"
  uri                     = "${aws_lambda_function.coin-changer-2.invoke_arn}"
  integration_http_method = "POST"
}

resource "aws_api_gateway_deployment" "coin-changer-2-api" {
  depends_on = [
    "aws_api_gateway_integration.changer"
  ]

  rest_api_id = "${aws_api_gateway_rest_api.coin-changer-2-api.id}"
  stage_name  = "test"
}

output "base_url" {
  value = "${aws_api_gateway_deployment.coin-changer-2-api.invoke_url}"
}