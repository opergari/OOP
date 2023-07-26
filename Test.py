class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

class Menu:
    def __init__(self, categories):
        self.categories = categories

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

# Создание блюд
dish1 = Dish("Цезарь", "Салат с курицей и заправкой", 9.99)
dish2 = Dish("Стейк", "Говяжий стейк со специями", 17.99)
dish3 = Dish("Чизкейк", "Десерт с ванильным соусом", 6.99)

# Создание категорий и добавление блюд в них
appetizers_category = MenuCategory("Закуски", [dish1])
main_dishes_category = MenuCategory("Основные блюда", [dish2])
desserts_category = MenuCategory("Десерты", [dish3])

# Создание меню и добавление категорий в него
menu = Menu([appetizers_category, main_dishes_category, desserts_category])

# Создание заказа
order = Order()

# Пример добавления и удаления блюд в заказе
order.add_item(dish1)
order.add_item(dish2)
order.remove_item(dish1)

# Подсчет общей стоимости заказа
total_price = order.calculate_total()

# Вывод меню ресторана
print("Меню ресторана:")
for category in menu.categories:
    print(category.name)
    for dish in category.dishes:
        print(f"- {dish.name}: {dish.price}$")