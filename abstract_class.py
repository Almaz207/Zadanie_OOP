from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @abstractmethod
    @property
    def price(self):
        """Абстрактный метод, для реализации сеттера"""
        pass

    @abstractmethod
    @price.setter
    def price(self):
        """Абстрактный метод для изменения цены"""
        pass
