import pytest


@pytest.fixture
def sample_binary_data():
    with open("example_data.txt", "r", encoding="utf-8") as f_obj:
        data = [item.strip() for item in list(f_obj.readlines())]

    return data
