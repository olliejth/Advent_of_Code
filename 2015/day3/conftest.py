import pytest


@pytest.fixture
def visited_houses():

    l = [
        (0, 0),
        (2, 3),
        (-10000000000000, 3)
    ]

    return l
