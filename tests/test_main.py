import sys
import pytest
from context import main


def test_correct_usage(capfd):
    out = launch(["main.py", "27"], capfd)
    assert out == "[20, 5, 2]\n"


def test_errors_if_no_arguments_passed(capfd):
    with pytest.raises(Exception):
        launch(["main.py"], capfd)


def test_errors_if_non_numeric_argument_passed(capfd):
    with pytest.raises(Exception):
        launch(["main.py", "wrong argument type"], capfd)


def launch(params, capfd):
    sys.argv = params
    main()
    out, err = capfd.readouterr()
    return out