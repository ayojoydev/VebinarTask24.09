def area(side):
    try:
        return side ** 2 * 6
    except ZeroDivisionError :
        return "Капец"

def volume (side):
    try:
        return side ** 3
    except ZeroDivisionError:
        return "Капец"