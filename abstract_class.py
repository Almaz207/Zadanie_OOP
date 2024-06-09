from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @property
    @abstractmethod
    def price(self):
        """Абстрактный метод, для реализации сеттера"""
        pass

    @price.setter
    @abstractmethod
    def price(self):
        """Абстрактный метод для изменения цены"""
        pass
