import sys
import pytest
from context import cli_main


def test_correct_usage(capfd):
    out = launch(["coin_changer.py", "27"], capfd)
    assert out == "[20, 5, 2]\n"


def test_errors_if_no_arguments_passed(capfd):
    with pytest.raises(Exception):
        launch(["coin_changer.py"], capfd)


def test_errors_if_non_numeric_argument_passed(capfd):
    with pytest.raises(Exception):
        launch(["coin_changer.py", "wrong argument type"], capfd)


def launch(params, capfd):
    sys.argv = params
    cli_main()
    out, err = capfd.readouterr()
    return out