# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]
    
def total_units(y_list : ShoppingList):
    sum1 = 0
    for i in range(y_list.number_of_items()):
        sum1 += y_list.amount(i)
    return sum1

# -------------------------
# Write your solution here:
# -------------------------

