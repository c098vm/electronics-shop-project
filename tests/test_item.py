"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src import item
import csv

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



