import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.all.append(self)


    def __repr__(self) -> str:
        """
        Возвращает информацию об объекте класса в режиме отладки.
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self) -> str:
        """
        Возвращает информацию об объекте класса для пользователей.
        """
        return self.__name


    def __add__(self, other) -> int:
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return self.quantity + other.quantity


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

    @property
    def name(self):
        """
        Возвращает наименование товара.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Устанавливает наименование товара, проверяя,
        что длина наименования не больше 10 символов.
        """
        if len(name) <= 10:
            self.__name = name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")


    @classmethod
    def instantiate_from_csv(cls) -> None:
        cls.all = []
        try:
            with open('../src/items.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls.all.append(cls(row['name'], float(row['price']), int(row['quantity'])))
        except FileNotFoundError:
            print("Файл не найден")


    @staticmethod
    def string_to_number(string):
        return int(float(string))
