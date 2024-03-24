import pytest

from classes import Category, Product


@pytest.fixture()
def pump():
    return Product("Pump", "Electric pump, 10 bar", 2000, 30)


@pytest.fixture()
def wrench():
    return Product("Wrench", "14 mm", 235.99, 115)


@pytest.fixture()
def tools(pump, wrench):
    return Category("Tools", "Auto repair tools", [pump, wrench])

def test_init_category(tools):
    assert tools.name == "Tools"
    assert tools.discription == "Auto repair tools"
    assert tools.products == [pump, wrench]

def test_init_product(product_tools):
    assert product_tools.name == "Pump"
    assert product_tools.discription == "Electric pump, 10 bar"
    assert product_tools.price == 2000
    assert product_tools.quantity_in_stock ==30


def test_quantity_category(tools):
    assert tools.quantity_category == 1


def test_quantity_products(tools):
    assert tools.quantity_products == 2