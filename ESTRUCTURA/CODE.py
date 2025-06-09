
import math
class Circle:
 """Class to represent a circle and calculate its properties"""

 def __init__(self, radius):
 """Initialize circle with given radius"""
 self.radius = radius

 def calculate_area(self):
 """Calculate circle area: A = πr²"""
 return math.pi * self.radius ** 2

 def calculate_perimeter(self):
 """Calculate circle perimeter (circumference): P = 2πr"""
 return 2 * math.pi * self.radius
class Rectangle:
 """Class to represent a rectangle and calculate its properties"""

 def __init__(self, length, width):
 """Initialize rectangle with given length and width"""
 self.length = length
 self.width = width

 def calculate_area(self):
 """Calculate rectangle area: A = length × width"""
 return self.length * self.width

 def calculate_perimeter(self):
 """Calculate rectangle perimeter: P = 2(length + width)"""
 return 2 * (self.length + self.width)

# Demonstration of the classes
if __name__ == "__main__":
 print("GEOMETRIC FIGURES CALCULATION DEMO\n")

 # Create and test a circle
 circle = Circle(5)
 print("=== CIRCLE (radius = 5) ===")
 print(f"Area: {circle.calculate_area():.4f}")
 print(f"Perimeter: {circle.calculate_perimeter():.4f}\n")

 # Create and test a rectangle
 rectangle = Rectangle(4, 6)
 print("=== RECTANGLE (4×6) ===")
 print(f"Area: {rectangle.calculate_area()}")
 print(f"Perimeter: {rectangle.calculate_perimeter()}")

 input("\nPress Enter to exit...") # Pause before closing