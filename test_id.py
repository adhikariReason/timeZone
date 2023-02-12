from id import sums


def test_sum():
	assert sums(1,2) == 3
	assert sums(-1,1) == 0