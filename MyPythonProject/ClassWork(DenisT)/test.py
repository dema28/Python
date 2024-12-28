import pytest
class TestToken:

    @pytest.mark.xfail(reason="Not implemented yet")
    def test_get_token(self, get_token):
        token = get_token
        print()
        print(token)
        # assert 1 == 2



    def test_get_token1(self, get_token):
        token = get_token
        print()
        print(token)

    def test_get_token2(self, get_token):
        token = get_token
        print()
        print(token)

    @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])
    def test_check_sum(self, a, b, c):
        assert a + b == c,f"Expected {a + b} but got {c}"