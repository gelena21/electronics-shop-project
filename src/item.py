import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: float) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """Геттер для получения значения атрибута name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
               Сеттер для установки значения атрибута name.

               :param value: Новое значение для name.
               """
        if len(value) <= 10:
            self._name = value[:10]
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        """
        Создает объекты Item из данных CSV-файла.

        :param filename: Имя CSV-файла.
        """
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name = row[0]
                price = cls.string_to_number(row[1])
                quantity = cls.string_to_number(row[2])
                item = Item(name, price, quantity)
                cls.all.append(item)

    @staticmethod
    def string_to_number(value: str, default: float = 0.0, raise_error: bool = False) -> float:
        """
        Преобразует строку в число.

        :param value: Строковое представление числа.
        :param default: Значение по умолчанию, возвращаемое при ошибке преобразования.
        :param raise_error: Флаг, указывающий, следует ли выбрасывать исключение при ошибке.
        :return: Преобразованное число.
        """
        try:
            return float(value)
        except ValueError:
            if raise_error:
                raise
            return default

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

