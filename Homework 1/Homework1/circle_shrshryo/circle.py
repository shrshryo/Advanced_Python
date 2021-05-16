import math

def programForAreaandCircumference(r):
    area = math.pi * r**2
    circumference = 2*math.pi*r
    return area, circumference

# r = int(input("Enter radius: "))
# if r < 1:
#     while(r<1):
#         r = int(input("Enter positive number, no negative: "))
# area, circumstance = areaAndCicumstenance(r)
# print("Area is " + str(area) + ".")
# print("Circumstance is " + str(circumstance) + ".")
