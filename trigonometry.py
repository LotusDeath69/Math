import math 
def cosineLawLength(a, b, degree):
  return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(degree)))


def cosineLawDegree(x, a, b):
  return math.degrees(math.acos((x**2 - a**2 - b**2) / (-2*b*a)))


print(cosineLawLength(15, 20, 60))  
print(cosineLawDegree(9.6, 100, 100))
  