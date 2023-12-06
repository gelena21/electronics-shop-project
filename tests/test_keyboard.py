from src.item import Item
from src.keyboard import Keyboard, LanguageMixin
import pytest


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_inherits_from_item(keyboard):
    assert isinstance(keyboard, Item)


def test_keyboard_str_representation(keyboard):
    assert str(keyboard) == "Dark Project KD87A"


def test_keyboard_language_default(keyboard):
    assert keyboard.language == LanguageMixin.EN


def test_keyboard_change_language(keyboard):
    keyboard.change_lang(LanguageMixin.RU)
    assert keyboard.language == LanguageMixin.RU

    keyboard.change_lang(LanguageMixin.EN)
    assert keyboard.language == LanguageMixin.EN


def test_keyboard_change_language_invalid_value_raises_error(keyboard):
    with pytest.raises(ValueError, match="Unsupported language"):
        keyboard.change_lang("CH")


def test_keyboard_set_language(keyboard):
    keyboard.language = LanguageMixin.RU
    assert keyboard.language == LanguageMixin.RU

    keyboard.language = LanguageMixin.EN
    assert keyboard.language == LanguageMixin.EN


def test_keyboard_set_invalid_language_raises_error(keyboard):
    with pytest.raises(ValueError, match="Unsupported language"):
        keyboard.language = "CH"
