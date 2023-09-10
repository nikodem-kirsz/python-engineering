"""
GUI Framework: Create different types of UI elements (e.g., buttons, text fields) 
using a factory based on user preferences or platform-specific requirements.

Document Converters: Convert documents (e.g., PDF to text, HTML to PDF) using a factory 
to produce the appropriate converter based on the input format.
"""
from abc import ABC, abstractmethod

# Define an abstract base class for vehicles
class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

# Concrete classes for different types of vehicles
class Car(Vehicle):
    def create(self):
        return "Car"

class Bicycle(Vehicle):
    def create(self):
        return "Bicycle"

# Factory class for creating vehicles
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type.lower() == "car":
            return Car()
        elif vehicle_type.lower() == "bicycle":
            return Bicycle()
        else:
            raise ValueError("Invalid vehicle type")

# Client code
factory = VehicleFactory()

vehicle1 = factory.create_vehicle("car")
print(f"Vehicle 1: {vehicle1.create()}")  # Output: Vehicle 1: Car

vehicle2 = factory.create_vehicle("bicycle")
print(f"Vehicle 2: {vehicle2.create()}")  # Output: Vehicle 2: Bicycle
