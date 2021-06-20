# pip install pytest-repeat
import pytest 

@pytest.mark.repeat(100)
def test_instance_generator():
    pass