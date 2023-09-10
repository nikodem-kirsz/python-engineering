import copy

# Prototype interface
class ShapePrototype:
    def clone(self):
        pass

# Concrete prototype for a Circle
class Circle(ShapePrototype):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        # Use the built-in copy module to create a shallow copy
        return copy.copy(self)

    def __str__(self):
        return f"Circle with radius {self.radius}"

# Concrete prototype for a Rectangle
class Rectangle(ShapePrototype):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def clone(self):
        # Use the built-in copy module to create a shallow copy
        return copy.copy(self)

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

# Client code
circle_prototype = Circle(5)
rectangle_prototype = Rectangle(4, 6)

# Create new shapes by cloning the prototypes
new_circle = circle_prototype.clone()
new_rectangle = rectangle_prototype.clone()

# Modify the cloned objects (shallow copy)
new_circle.radius = 3
new_rectangle.width = 5

# Print the shapes
print(circle_prototype)     # Original circle with radius 5
print(rectangle_prototype)  # Original rectangle with width 4 and height 6
print(new_circle)           # Cloned circle with radius 3
print(new_rectangle)        # Cloned rectangle with width 5 and height 6


"""
The Prototype Pattern can boost efficiency in several ways:

Reduced Object Creation Overhead: Creating an object can be an expensive operation, 
especially when it involves complex initialization processes or resource allocation. 
With the Prototype Pattern, you create new objects by copying existing ones, 
which can be much faster and less resource-intensive than creating objects from scratch.

Consistency and Reusability: By using prototypes, you ensure that the new objects start 
with a consistent initial state. This consistency can be particularly important in scenarios
where objects share common configurations or settings. It also encourages code reuse since 
you're reusing existing objects as templates.

Minimized Initialization Logic: Some objects require complex initialization logic that is 
performed during object creation. By using prototypes, 
you can avoid repeating this initialization logic for each new object and instead 
copy an already initialized prototype.

Dynamic Object Creation: The Prototype Pattern allows you to create new objects at 
runtime based on the state of existing objects. This flexibility is useful when the 
exact type or configuration of the new object is determined dynamically.

Resource Efficiency: In scenarios where system resources are limited, such as 
in embedded systems or real-time applications, creating objects by cloning prototypes
 can be more efficient in terms of memory and processing power.

Improved Performance: Since cloning an object is typically faster than constructing it, 
the Prototype Pattern can lead to improved application performance, especially in situations 
where objects need to be created frequently.

Simplified Object Construction: In cases where constructing objects involves complex 
interactions with other components or subsystems, using prototypes can simplify the 
construction process and ensure that the new objects are correctly configured.

Overall, the Prototype Pattern optimizes object creation by reusing existing objects 
as templates and minimizing the overhead associated with object construction. 
This efficiency is particularly valuable in scenarios where object creation is a critical 
performance factor or where consistent object initialization is important.
"""