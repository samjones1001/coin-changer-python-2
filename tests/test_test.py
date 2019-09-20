from context import changer

def test_passing_0_returns_an_empty_list():
    assert changer.calculate(0) == []

def test_passing_1_returns_a_single_penny():
    assert changer.calculate(1) == [1]

def test_passing_2_returns_2p():
    assert changer.calculate(2) == [2]

def test_passing_5_returns_5p():
    assert changer.calculate(5) == [5]

def test_passing_10_returns_10p():
    assert changer.calculate(10) == [10]

def test_passing_20_returns_20p():
    assert changer.calculate(20) == [20]

def test_passing_50_returns_50p():
    assert changer.calculate(50) == [50]

def test_passing_100_returns_1_pound():
    assert changer.calculate(100) == [100]

def test_passing_200_returns_2_pounds():
    assert changer.calculate(200) == [200]

def test_correct_combination_of_two_coins_where_needed():
    assert changer.calculate(3) == [2, 1]
    assert changer.calculate(6) == [5, 1]
    assert changer.calculate(25) == [20 ,5]