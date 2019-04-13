import math

a = float(input())
b = float(input())

c = a*b;

print(int(c - math.floor(c/109)* 109))