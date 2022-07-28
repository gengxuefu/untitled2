import pytest

@pytest.fixture()
def login():
    usname = 'liudehua'
    return usname


@pytest.mark.parametrize('a,b',[(1,2),(10,20),(90,100)])
class Testoub:
    def func(self,x):
        return x + 1

    def test_func(self,a,b,login):
        assert self.func(a) == b
        print(f"{login}")

    def test_funb(self,a,b):
        assert self.func(a) == b

    def test_funb(self,a,b):
        assert self.func(a) == b