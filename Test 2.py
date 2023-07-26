class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.price}UAH\nDescription: {self.description}"

class Category:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __str__(self):
        category_info = [f"{self.name}:"]
        for dish in self.dishes:
            category_info.append(str(dish))
        return "\n".join(category_info)
class Menu:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def __str__(self):
        menu_info = []
        for category in self.categories:
            menu_info.append(str(category))
        return "\n".join(menu_info)

class Order:
    def __init__(self):
        self.items = []

    def add_dish(self, item):
        self.items.append(item)

    def calculate_total(self):
        total_cost = sum(dish.price for dish in self.items)
        return total_cost
    def __str__(self):
        if not self.items:
            return "The order is empty."
        order_info = [f"Ordered items:"]
        for dish in self.items:
            order_info.append(str(dish))
        total_cost = self.calculate_total()
        order_info.append(f"Total cost: ${total_cost:.2f}")
        return "\n".join(order_info)

dish1 = Dish("Caesar Salad", "Fresh romaine lettuce with croutons, parmesan cheese, and Caesar dressing.", 9.99)
dish2 = Dish("Spaghetti Bolognese", "Classic Italian pasta with meat sauce.", 12.99)
dish3 = Dish("Cheesecake", "Delicious New York-style cheesecake with raspberry sauce.", 7.99)

appetizers = Category("Appetizers")
appetizers.add_dish(dish1)

main_courses = Category("Main Courses")
main_courses.add_dish(dish2)

desserts = Category("Desserts")
desserts.add_dish(dish3)

menu = Menu()
menu.add_category(appetizers)
menu.add_category(main_courses)
menu.add_category(desserts)

order = Order()
order.add_dish(dish1)
order.add_dish(dish2)
order.add_dish(dish3)

print("Welcome to Our Restaurant!")
print("Menu:")
print(menu)
print("\nCustomer's Order:")
print(order)