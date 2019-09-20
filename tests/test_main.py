import sys
from context import main

def test_correct_usage(capfd):
    out = launch(["main.py", "27"], capfd)
    assert out == "[20, 5, 2]\n"

def launch(params, capfd):
    sys.argv = params
    main()
    out, err = capfd.readouterr()
    return out