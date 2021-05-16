import math

def areaAndCicumstenance(radius):
    area = math.pi * radius**2
    circumstance = 2*math.pi*radius
    return area, circumstance

r = int(input("Enter radius: "))
if r < 1:
    while(r<1):
        r = int(input("Enter positive number, no negative: "))
area, circumstance = areaAndCicumstenance(r)
print("Area is " + str(area) + ".")
print("Circumstance is " + str(circumstance) + ".")
