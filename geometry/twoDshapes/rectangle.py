import math
def area(side):
    try:
        return side ** 2
    except ZeroDivisionError :
        return "Капец"

def perimetr(side):
    try:
        return side * 4
    except ZeroDivisionError :
        return "Капец"