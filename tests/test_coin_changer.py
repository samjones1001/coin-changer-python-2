import sys
import pytest
from coin_changer import cli_main, lambda_main


class Runner():
    def __init__(self, capfd):
        self._capfd = capfd

    def run(self, *args):
        sys.argv = ["coin_changer.py", *args]
        cli_main()
        out,err = self._capfd.readouterr()

        if err is not None:
            print(err)

        return out


@pytest.fixture
def app(capfd):
    return Runner(capfd)


def test_correct_usage(app):
    out = app.run("27")
    assert out == "[20, 5, 2]\n"


def test_errors_if_no_arguments_passed(capfd):
    with pytest.raises(Exception):
        app.run()


def test_errors_if_non_numeric_argument_passed(capfd):
    with pytest.raises(Exception):
        app.run("wrong argument type")


def can_be_run_from_lambda_entry_point():
    event = {
        'queryStringParameters': {
            'change_amount': 25
        }
    }

    expected_output = {
        'statusCode': 200,
        'body': '[20, 5]'
    }
    assert lambda_main(event, {}) == expected_output
