from src.item import Item


class MixinChangeLang:
    """
    Класс-миксин для хранения и изменения языка.
    """

    LANGUAGE = "EN"

    def __init__(self):
        self.__language = self.LANGUAGE

    @property
    def language(self):
        """
        Геттер для получения текущего языка.
        """
        return self.__language

    def change_lang(self):
        """
        Метод для замены языка.
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class KeyBoard(Item, MixinChangeLang):
    """
    Класс для клавиатуры.
    """
    pass
