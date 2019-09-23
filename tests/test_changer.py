from changer import changer


def test_passing_0_returns_an_empty_list():
    assert changer.change(0) == []


def test_passing_1_returns_a_single_penny():
    assert changer.change(1) == [1]


def test_passing_2_returns_2p():
    assert changer.change(2) == [2]


def test_passing_5_returns_5p():
    assert changer.change(5) == [5]


def test_passing_10_returns_10p():
    assert changer.change(10) == [10]


def test_passing_20_returns_20p():
    assert changer.change(20) == [20]


def test_passing_50_returns_50p():
    assert changer.change(50) == [50]


def test_passing_100_returns_1_pound():
    assert changer.change(100) == [100]


def test_passing_200_returns_2_pounds():
    assert changer.change(200) == [200]


def test_returns_correct_combination_of_two_coins_where_needed():
    assert changer.change(3) == [2, 1]
    assert changer.change(6) == [5, 1]
    assert changer.change(25) == [20 ,5]


def test_returns_correct_combination_of_three_coins_where_needed():
    assert changer.change(42) == [20, 20, 2]
    assert changer.change(23) == [20, 2, 1]
    assert changer.change(112) == [100, 10, 2]


def test_returns_correct_combination_of_coins_in_complex_cases():
    assert changer.change(327) == [200, 100, 20, 5, 2]
    assert changer.change(159) == [100, 50, 5, 2, 2]
    assert changer.change(73) == [50, 20, 2, 1]

