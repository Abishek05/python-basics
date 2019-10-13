from math import pi

radius = float(input("Enter the radius:"))


def area_of_circle(radius):
    area = pi * (radius ** 2)
    return area


area = area_of_circle(radius)
print(area)

