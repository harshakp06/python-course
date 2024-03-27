import math

def circle_stats(radius):
    area = round((math.pi* (radius ** 2)),2)
    circum = round((2 * math.pi * radius),3)
    return area, circum

rad = int(input("enter radius of circle: "))

# d = 2
a, c = circle_stats(rad)
# a = round(a,d)

print(f"area {a} and circumference {c}")