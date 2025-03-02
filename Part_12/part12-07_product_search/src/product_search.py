# Write your solution here


def search(products : list, criterions : callable):
    return [i for i in products if criterions(i)]

def price_under_4_euros(product):
    if(product[1] < 4):
        return True
