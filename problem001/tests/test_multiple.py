from solution.multiple import gen_multiples_set


def test_gen_multiple_set():
    expected = set([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])
    assert gen_multiples_set(3, limit=30) != expected

    expected = set([3, 6, 9, 12, 15, 18, 21, 24, 27])
    assert gen_multiples_set(3, limit=30) == expected
