"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def first_item():
    return Item("Изделие", 149.99, 2)


def test_apply_discount(first_item):
    first_item.apply_discount()
    assert first_item.price == 149.99


def test_calculate_total_price(first_item):
    assert first_item.calculate_total_price() == 299.98


def test_name_setter_length_limit():
    item = Item("ShortName", 99.99, 1)
    assert item.name == "ShortName"

    with pytest.raises(ValueError, match="Длина наименования товара превышает 10 символов."):
        item.name = "TooLongNameToExceedTheLimit"


def test_instantiate_from_csv():
    csv_data = "Phone,199.99,3\nLaptop,899.99,1\n"
    with open("test_items.csv", "w", encoding="utf-8") as csv_file:
        csv_file.write(csv_data)
