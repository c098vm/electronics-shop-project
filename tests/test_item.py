"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src import item, phone


def test_calculate_total_price():
    item1 = item.Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1 = item.Item("Смартфон", 10000, 20)
    item.Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_string_to_number():
    assert item.Item.string_to_number('5') == 5
    assert item.Item.string_to_number('5.0') == 5
    assert item.Item.string_to_number('5.5') == 5


def test_name():
    item1 = item.Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    item1.name = "Монитор"
    assert item1.name == "Монитор"


def test_repr():
    item1 = item.Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = item.Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = item.Item("Смартфон", 10000, 20)
    phone1 = phone.Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10