# Budget App (Category & Spending Chart)

This project is a Python-based budget tracking application that allows users to manage spending across multiple categories. It supports deposits, withdrawals, transfers between categories, and generates a text-based chart that visualizes the percentage of spending per category.

The project focuses on practicing object-oriented programming, data structures, and formatted output in Python.

---

## Features

- Create budget categories (e.g. Food, Clothing, Auto)
- Record deposits and withdrawals with descriptions
- Transfer funds between categories
- Track balances for each category
- Generate a percentage-based spending chart
- Clean, readable formatted output

---

## File Structure

budget.py

README.md

---

## How It Works

### Category Class

Each budget category is represented by a `Category` object that contains:
- A category name
- A ledger that stores all transactions as dictionaries with `amount` and `description`

The class supports the following methods:
- `deposit(amount, description="")`
- `withdraw(amount, description="")`
- `transfer(amount, category)`
- `get_balance()`
- `check_funds(amount)`
- `__str__()` for formatted printing of the ledger and total balance

---

### Spending Chart

The `create_spend_chart(categories)` function:
- Calculates total withdrawals for each category
- Converts spending into percentages
- Rounds percentages to the nearest 10
- Displays a vertical chart showing relative spending by category

The chart provides a simple visualization directly in the terminal.

---

## Running the Program

Make sure you have Python 3 installed.

```bash
python budget.py
The main() function demonstrates example usage by:
Creating multiple categories
Making deposits and withdrawals
Transferring funds between categories
Printing the spending chart
Example Usage
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(15.89, "restaurant")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
Concepts Practiced
Object-oriented programming (classes and methods)
Python dictionaries and lists
Control flow and iteration
String formatting and alignment
Modular function design
