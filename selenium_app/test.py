import pytest

@pytest.fixture()
def m():
    print("setup")
    m = 3
    yield m
    print("teardown")

#@pytest.mark.parametrize(["a","b"],[(1,1),(2,2)])
def test_my_test(m):
    print(m)


