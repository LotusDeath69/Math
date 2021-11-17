import math 
def cosineLawLength(a, b, degree):
  return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(degree)))


def cosineLawDegree(x, a, b):
  return math.degrees(math.acos((x**2 - a**2 - b**2) / (-2*b*a)))


print(cosineLawLength(3, 2.5, 34))  
print(cosineLawDegree(7, 4, 6))  