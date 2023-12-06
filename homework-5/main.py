from src.keyboard import Keyboard, LanguageMixin

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang(LanguageMixin.RU)
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang(LanguageMixin.EN)
    assert str(kb.language) == "EN"

    try:
        kb.language = 'CH'
    except ValueError as e:
        assert str(e) == "Unsupported language"
    else:
        raise AssertionError("Expected ValueError but got no exception")
    # AttributeError: property 'language' of 'Keyboard' object has no setter
