import math

squares = []
# Squares increment faster than triangles, so while we need a list of
# squares, we can get by with a single triangle
triangle = 0

maxNum = 1000000

for i in range(0,maxNum):
    squares.append(i * i)
    triangle = (i * (i + 1)) / 2
    
    for j in squares:
        if triangle > j:
            squares.remove(j)
        elif triangle == j:
            print "Match found: triangle-square equals " + str(triangle)
            print "The squared number is " + str(int(math.sqrt(j)))
            print "The triangle number is " + str(i)