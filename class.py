# class Meal:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} — {self.price} сум"


# class Order:
#     def __init__(self):
#         self.meals = []

#     def add_meal(self, meal):
#         self.meals.append(meal)

#     def total(self):
#         return sum(meal.price for meal in self.meals)

#     def __str__(self):
#         lines = ["Заказ:"]
#         for meal in self.meals:
#             lines.append(f"  - {meal.name}: {meal.price} сум")
#         lines.append(f"Итого: {self.total()} сум")
#         return "\n".join(lines)


# class Restaurant:
#     def __init__(self):
#         self.orders = []

#     def add_order(self, order):
#         self.orders.append(order)

#     def daily_income(self):
#         return sum(order.total() for order in self.orders)

#     def print_daily_report(self):
#         print("\nОтчёт за день:\n")

#         if not self.orders:
#             print("Заказов нет.")
#             return

#         for i, order in enumerate(self.orders, 1):
#             print(f"--- Заказ #{i} ---")
#             print(order)
#             print()

#         print(f"Общая дневная выручка: {self.daily_income()} сум\n")

# restaurant = Restaurant()

# print("=== Ресторан: ввод заказов ===")

# while True:
#     order = Order()
#     print("\nСоздаём новый заказ.")

#     while True:
#         name = input("Название блюда (или 'стоп' чтобы закончить заказ): ")
#         if name.lower() == "стоп":
#             break

#         price = int(input("Цена блюда: "))
#         meal = Meal(name, price)
#         order.add_meal(meal)

#     restaurant.add_order(order)

#     more = input("Добавить ещё один заказ? (да/нет): ")
#     if more.lower() != "да":
#         break

# restaurant.print_daily_report()
