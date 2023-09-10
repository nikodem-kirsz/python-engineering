# Define components of a meal
class Burger:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.size} Burger"

class Fries:
    def __str__(self):
        return "Fries"

class Drink:
    def __init__(self, size, kind):
        self.size = size
        self.kind = kind

    def __str__(self):
        return f"{self.size} {self.kind} Drink"

# Meal builder
class MealBuilder:
    def __init__(self):
        self.meal = []

    def add_burger(self, size):
        self.meal.append(Burger(size))
        return self  # Return self for method chaining

    def add_fries(self):
        self.meal.append(Fries())
        return self

    def add_drink(self, size, kind):
        self.meal.append(Drink(size, kind))
        return self

    def build(self):
        return self.meal

# Usage
builder = MealBuilder()
my_meal = builder.add_burger("Large").add_fries().add_drink("Medium", "Soda").build()

print("My Custom Meal:")
for item in my_meal:
    print(item)
