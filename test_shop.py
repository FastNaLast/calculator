from shop import Cart, discount
import sys
import pytest

@pytest.mark.skip(reason="не готова")
def test_discount():
    assert discount(100, 20) == 80  



@pytest.mark.skipif(sys.platform != "win32",reason="не винда")
def test_discount2():
    assert discount(100, 20) == 80 

@pytest.mark.xfail(raises=ZeroDivisionError,reason="на ноль дели")
def test_discount3():
    assert discount(100, 30) == 70

@pytest.mark.xfail(raises=ZeroDivisionError,reason="на ноль дели")
def test_discount4():
    assert discount(100, 20,d=False) == 80 
@pytest.fixture
def cart():
    c = Cart()
    c.add('Milk',50,2)
    c.add('Bread',1,100)
    return c

def test_total(cart):
    assert cart.total() == 200
def test_total(cart):
    assert cart.total(10) == 180