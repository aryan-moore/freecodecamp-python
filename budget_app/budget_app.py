class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        dpsit = {'amount': amount, 'description': description}
        self.ledger.append(dpsit)
        return

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount*-1, 'description': description})
            return True
        else:
            return False
            

    def get_balance(self):
        sum = 0
        for entry in self.ledger:
            sum += entry['amount']
        return sum
        
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        

    def check_funds(self, amount):
        return True if amount <= self.get_balance() else False

    def __str__(self):
        namelength = len(self.name)
        numstars = "*" * ((30 - namelength)//2)
        output = numstars + self.name + numstars + "\n"
        for entry in self.ledger:
            items = list(entry.items())
            right = items[0][1]
            right = "{:.2f}".format(right)
            left = items[1][1]
            left = left[:23]
            right = (str(right))[:7]
            spaces = 30 - len(left) - len(right)
            output += left + spaces*" " + right + "\n"
        output += "Total: " + str(self.get_balance())
        return output

def main():
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    car = Category('Auto')
    car.deposit(10000, 'deposit')
    car.withdraw(28, 'car')
    categories = [food, clothing, car]
    print(create_spend_chart(categories))


def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    totals = []
    names = []
    nameslengths = []
    for category in categories:
        names.append(category.name)
        nameslengths.append(len(category.name))
        total = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                total += entry['amount']
        totals.append(total)
    totalsum = sum(totals)
    percentages = []
    for t in totals:
        t = t / totalsum * 100
        t = round(t)
        percentages.append(t)
    for i in range(100, -1, -10):
        stringi = str(i)
        output += " "*(3-len(stringi)) + str(i) + "| "
        for p in percentages:
            if(p >= i):
                output += "o  "
            else:
                output += "   "
        output += "\n"
    output += "    " + "---"*len(categories) + '-\n'
    longestname = max(names, key = len)
    for c in range(len(longestname)):
        output += "     "
        for n in range(len(names)):
            if c < nameslengths[n]:
                output += names[n][c] + "  "
            else:
                output += "   "
        if (c == len(longestname) - 1):
            pass
        else:
            output += "\n"

    return output
    

main()
