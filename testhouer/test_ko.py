import pytest

@pytest.fixture()
def login():
    username = '刘德华'
    return username


@pytest.mark.parametrize('a,b',[(1,2),(3,4),('a','b')])
class Testod():
    def sorto(self,x):
        return x + 1

    def test_pp(self,a,b,login):
        assert self.sorto(a) == b
        print(f"姓名=={login}")

    def test_po(self,a,b):
        assert self.sorto(a) != b

    def test_pq(self,a,b):
        assert self.sorto(a) >= b
