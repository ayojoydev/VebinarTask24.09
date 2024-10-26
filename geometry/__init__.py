from .twoDshapes.circle import area as circle_area, perimetr as circle_perimetr
from .twoDshapes.rectangle import area as rectangle_area, perimetr as rectangle_perimetr
from .twoDshapes.triangle import area as triangle_area, perimetr as triangle_perimetr
from .threeDshapes.sphere import area as sphere_area, volume as sphere_volume
from .threeDshapes.pyramid import area as pyramid_area, volume as pyramid_volume
from .threeDshapes.cube import area as cube_area, volume as cube_volume



__all__ = [
    "circle_area",
    "circle_perimetr",
    "rectangle_area",
    "rectangle_perimetr",
    "triangle_area",
    "triangle_perimetr",
    "sphere_area",
    "sphere_volume",
    "pyramid_area",
    "pyramid_volume",
    "cube_area",
    "cube_volume"
]