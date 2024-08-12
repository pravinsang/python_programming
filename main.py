from geometry.area import area_of_circle, DEFAULT_RADIUS
from geometry.calculations import add

a = 10
b = 20
radius = 2.4
print(f"Sum = {add(a, b)}")
print(f"Area of circle = {area_of_circle(radius)}")
print(f"Area of circle = {area_of_circle(radius=DEFAULT_RADIUS)}")

