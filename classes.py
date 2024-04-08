class Category:
    name: str
    discription: str
    products: list

    quantity_category = 0
    quantity_products = 0

    def __init__(self, name: str, discription: str, products: list):
        self.name = name
        self.discription = discription
        self.__products = products

        Category.quantity_category += 1
        Category.quantity_products += len(self.__products)

    @property
    def add_product_at_list(self, object_product):
        return f'{object_product}, будет добавлен в категорию {self.name}'

    @add_product_at_list.setter
    def add_product_at_list(self, object_product):
        self.__products.append(object_product)
        Category.quantity_products += 1

    @property
    def return_product(self):
        for product in self.__products:
            return f'{product}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.'


class Product:
    name: str
    discription: str
    price: float
    quantity_in_stock: int

    def __init__(self, name: str, discription: str, price: float, quantity_in_stock: int):
        self.name = name
        self.discription = discription
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def creat_product(cls, name, description, price, quantity_in_stock):
        return cls(name, description, price, quantity_in_stock)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price
