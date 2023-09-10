"""
Text Formatting: Enhance plain text with decorators like bold, italics, or underline 
to generate formatted documents.

Security: Add layers of security to components, such as encryption or authentication, 
without altering their core functionality.
"""

# Base Coffee class
class Coffee:
    def cost(self):
        return 5 # Basic coffee costs $5

# Decorator for adding milk
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2 # Add $2 for milk 

# Decorator for adding sugar
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1 # Add $1 for sugar          

class CostLoggerDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        cost = self._coffee.cost()
        print(f"Cost of coffee: ${cost}")
        return cost

# Create a basic coffee
coffee = Coffee()

# Add decorators to customize the coffee
coffee_with_milk = MilkDecorator(coffee)
coffee_with_sugar = SugarDecorator(coffee)
coffee_with_milk_and_sugar = MilkDecorator(SugarDecorator(coffee))

# Add a cost logger decorator
coffee_with_logger = CostLoggerDecorator(MilkDecorator(SugarDecorator(Coffee())))

# Calculate and log the cost
cost = coffee_with_logger.cost()
