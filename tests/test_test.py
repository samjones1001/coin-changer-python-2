from context import changer

def test_passing_0_returns_an_empty_list():
    assert changer.calculate(0) == []

def test_passing_1_returns_a_single_penny():
    assert changer.calculate(1) == [1]