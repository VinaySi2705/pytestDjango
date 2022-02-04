import pytest

@pytest.fixture
def yield_fixture():
    print('Start Test')
    yield 6
    print('End Test')

def test_example(yield_fixture):
    print('run-example-1')
    assert yield_fixture == 6
