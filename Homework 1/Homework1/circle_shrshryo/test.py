import sys
sys.path.append('../')
from circle_shrshryo import circle
r = int(input("Enter the radius: "))
if r < 1:
    while(r<1):
        r = int(input("Enter positive number, no negative: "))
ans = circle.programForAreaandCircumference(r)
print(ans)