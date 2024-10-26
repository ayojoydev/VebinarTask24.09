import math
def area(radius):
    try:
        return 4 * math.pi * radius ** 2
    except ZeroDivisionError :
        return "Капец"

def volume (radius):
    try:
        return 3/4*math.pi * radius** 3
    except ZeroDivisionError :
        return "Капец"