from abstract_class import AbstractProduct


class Category:
    """Категория товаров"""
    name: str
    discription: str
    products: list

    quantity_category = 0
    quantity_products = 0

    def __init__(self, name: str, discription: str, products: list):
        self.name = name
        self.discription = discription
        self.products = products

        Category.quantity_category += 1  # подсчёт количества категорий
        Category.quantity_products += len(self.products)  # подсчёт видов товаров в категории

    def __str__(self):
        """Отображение при печати объекта класса"""
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        """Выводит информацию об общем количестве продуктов конкретной категории на складе """
        total_products = 0
        for product in self.products:
            total_products += product.quantity_in_stock
            return total_products

    @property
    def add_product_at_list(self):
        """Это геттер, для сеттера"""
        return self.name

    @add_product_at_list.setter
    def add_product_at_list(self, object_product):
        """Внесение продукта(товара) в список"""
        if isinstance(object_product, Product):
            self.products.append(object_product)
            Category.quantity_products += 1
        else:
            raise TypeError(
                "Можно добавлять только обекты класса 'Product' или обекты дочерних классов класса 'Product'")

    @property
    def return_product(self):
        """Геттер, который воззвращает наименование продукта, его цену и остаток на складе"""
        for product in self.products:
            print(f'{product}!')


class Product(AbstractProduct):
    """Товары(продукты)"""
    name: str
    discription: str
    price: float
    quantity_in_stock: int

    def __init__(self, name: str, discription: str, price: float, quantity_in_stock: int):
        self.name = name
        self.discription = discription
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def __str__(self):
        """Дандер метод для отображения информации о цене и остатках товара"""
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт.'

    @classmethod
    def creat_product(cls, name, description, price, quantity_in_stock):
        """Классметод который инициирует создание нового экземпляра класса Продукт"""
        return cls(name, description, price, quantity_in_stock)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер, который меняет цену продукта, но только если она корректная"""
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price

    def __add__(self, other):
        """Метод выполняется при сложении двух объектов одного класса
        (Нельзя сложить объект родительского и дочернего класса) и
        вернет сумму произведений количества на цену двух этих объектов"""
        if type(self) is type(other):
            return self.price * self.quantity_in_stock + other.price * other.quantity_in_stock
        else:
            raise TypeError


class Smartphone(Product):
    """Дочерний класс класса Продукт"""

    def __init__(self, name: str, discription: str, price: float, quantity_in_stock: int, performance, model, memory,
                 color):
        super().__init__(name, discription, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class Grass(Product):
    """Дочерний класс класса Продукт"""

    def __init__(self, name: str, discription: str, price: float, quantity_in_stock: int, country, germination_period,
                 color):
        super().__init__(name, discription, price, quantity_in_stock)
        self.country = country
        self.germination_period = germination_period
        self.color = color
