import math
def area(radius):
    try:
        return math.pi * radius ** 2
    except ZeroDivisionError :
        return "Капец"

def perimetr(radius):
    try:
        return 2 * math.pi * radius
    except ZeroDivisionError :
        return "Капец"