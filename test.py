class Product():
    def __init__(self, id, category, name, maker, color, price, description, rating):
        self.id = id                                #id
        self.category = category                    #Категория
        self.name = name                            #Наименование
        self.maker = maker                          #Производитель
        self.color = color                          #Окрас
        self.price = price                          #Цена
        self.description = description              #Описание
        self.rating = rating                        #Рейтинг

Products = [
    Product(1, "Телефоны", "Iphone 13 PRO Max", "Apple", "Серебристый", "110 990 ₽", 'Стандартное описание', "9.6"), #Пример
    Product(2, "Категория", "Название", "Производитель", "Цвет", "Цена ₽", "Стандартное описание", "Рейтинг"),    
    Product(3, "Категория", "Название", "Производитель", "Цвет", "Цена ₽", "Стандартное описание", "Рейтинг"),
    Product(4, "Категория", "Название", "Производитель", "Цвет", "Цена ₽", "Стандартное описание", "Рейтинг"),
]

filtered_products = list(filter(lambda p: len(p.name) > 5, Products))
names = [p.name for p in filtered_products]
print(names)