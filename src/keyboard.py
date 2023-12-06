from src.item import Item


class LanguageMixin:
    EN = 'EN'
    RU = 'RU'

    def __init__(self):
        self._language = self.EN

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_lang):
        self.change_lang(new_lang)

    def change_lang(self, new_lang=None):
        if new_lang is not None and new_lang in [self.EN, self.RU]:
            self._language = new_lang
        else:
            raise ValueError("Unsupported language")


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)
