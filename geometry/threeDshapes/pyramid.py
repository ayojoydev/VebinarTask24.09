
def area(side, h):
    try:
        return side*(side + 2 * h)
    except ZeroDivisionError :
        return "Капец"

def volume (side, H):
    try:
        return 1/3 * side ** 2 * H
    except ZeroDivisionError :
        return "Капец"