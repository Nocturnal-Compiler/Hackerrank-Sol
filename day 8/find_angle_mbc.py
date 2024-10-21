
import math

AB = int(input())
BC = int(input())

tan = (math.atan(AB/BC))
theta = round(math.degrees(tan))

print(theta,chr(176), sep = "")