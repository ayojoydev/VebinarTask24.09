#   geometry
#   |___init__.py
#   |_twoDShapes
#   |   |_ rectangle.py
#   |   |_ circle.py
#   |   |_ triangle.py
#   |
#   |_threeDshpaes
#   |   |_ cupe.py
#   |   |_ sphere.py
#   |   |_ pyramid.py
#   |
#   |
#   main.py

from geometry import circle_area, rectangle_area,triangle_area, circle_perimetr, rectangle_perimetr, triangle_perimetr,\
    sphere_area,sphere_volume,pyramid_area,pyramid_volume,cube_area,cube_volume

print(circle_area(0))
print(rectangle_area(12))
print(triangle_area(0))
print(circle_perimetr(12))
print(rectangle_perimetr(12))
print(triangle_perimetr(12))
print(sphere_area(12))
print(sphere_volume(12))
print(pyramid_area(12, 2))
print(pyramid_volume(12, 2))
print(cube_area(12))
print(cube_volume(12))

