import pytest
from generic.functs.math_functs import s_add

def test_s_add():
    res = s_add(6 , 7)
    assert res == 13
