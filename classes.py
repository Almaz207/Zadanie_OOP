
class Category:
    name: str
    discription: str
    products: list

    quantity_category = 0
    quantity_products = 0

    def __init__(self, name: str, discription: str, products: list):
        self.name = name
        self.discription = discription
        self.products = products

        Category.quantity_category += 1
        Category.quantity_products += len(products)


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
