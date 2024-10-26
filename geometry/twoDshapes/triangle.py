import math
def area(side):
    try:
        return side ** 2 / 2
    except ZeroDivisionError :
        return "Капец"

def perimetr(side):
    try:
        return side * 3
    except ZeroDivisionError :
        return "Капец"