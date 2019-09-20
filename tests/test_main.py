import sys
from context import main

def test_correct_usage(capfd):
    out = launch(["main.py", "27"], capfd)
    assert out == "[20, 5, 2]\n"


def test_errors_if_no_arguments_passed(capfd):
    out = launch(["main.py"], capfd)
    assert out == "Please provide a numeric argument\n"


def test_errors_if_non_numeric_argument_passed(capfd):
    out = launch(["main.py", "wrong argument type"], capfd)
    assert out == "Please provide a numeric argument\n"


def launch(params, capfd):
    sys.argv = params
    main()
    out, err = capfd.readouterr()
    return out