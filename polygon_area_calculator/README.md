# Shape Calculator (Rectangle & Square)

This project implements `Rectangle` and `Square` classes in Python to model geometric shapes and compute their properties. It demonstrates object-oriented programming concepts such as inheritance, method overriding, and encapsulation.

The project allows users to calculate area, perimeter, diagonal length, visualize shapes using text output, and determine how many smaller shapes fit inside larger ones.

---

## Features

### Rectangle
- Set width and height
- Calculate area, perimeter, and diagonal length
- Generate a text-based picture of the rectangle
- Determine how many smaller rectangles fit inside
- Clean string representation

### Square
- Inherits from `Rectangle`
- Ensures width and height remain equal
- Supports setting side length
- Overrides setters and string representation

---

## File Structure

shape_calculator.py
README.md

---

## How It Works

### Rectangle Class

The `Rectangle` class stores:
- `width`
- `height`

Supported methods:
- `set_width(value)`
- `set_height(value)`
- `get_area()`
- `get_perimeter()`
- `get_diagonal()`
- `get_picture()`
- `get_amount_inside(other)`
- `__str__()` for readable output

The `get_picture()` method prints the shape using asterisks (`*`) unless the dimensions exceed 50 units.

---

### Square Class

The `Square` class is a subclass of `Rectangle` that:
- Initializes both width and height to the same value
- Overrides setters to keep dimensions equal
- Adds a `set_side(length)` method
- Overrides `__str__()` for proper formatting

---

## Example Usage

```python
rect = Rectangle(10, 5)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_picture())

sq = Square(4)
sq.set_side(6)
print(sq)
Sample Output
Rectangle(width=10, height=5)
********************
********************
********************
********************
********************
Concepts Practiced
Object-Oriented Programming (OOP)
Class inheritance and method overriding
Mathematical computations
String formatting
Modular and reusable design
