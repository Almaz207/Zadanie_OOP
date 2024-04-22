#Добавлено специально для тестированияя правильности работы,
# что-то вроде модуля ручного тестирования, для личного пользования и илюстрации проблемы

from classes import Category, Product

tools = Category("Инструменты", "Auto repair tools", [])

product1 = Product("насос", "Electric pump, 10 bar", 2000, 30)
product1.price = 2050
print(product1)

product2 = Product("ключ", "14 mm", 235.99, 115)
product2.price = 250
print(product2)


tools.add_product_at_list = product1
tools.add_product_at_list = product2
#print(tools.return_product)

print(tools)
print(product1 + product2)
#В данном случае выводится
#насос, 2050 руб. Остаток: 30 шт.
#ключ, 250 руб. Остаток: 115 шт.
#Инструменты, количество продуктов: 30 шт. - должно быть не 30 штук, а 145
#Это подзадание первого задания
#90250
print(product1 + product2)

