import math

sqr = lambda x: math.pow(x, 2)
error = 0.001

# Find point of intersection
#
def intersection(point1, point2, plane, facet):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    equation, (A, B, C, D) = plane

    m = x2 - x1
    n = y2 - y1
    p = z2 - z1

    if A * m + B * n + C * p == 0: return None

    t = -(A * x1 + B * y1 + C * z1 + D) / (A * m + B * n + C * p)

    x = x1 + m * t
    y = y1 + n * t
    z = z1 + p * t

    point = (x, y, z)

    if accessory(point, facet): return point
    else: return None

def lightIntersection(point1, point2, plane, facet):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    dist = distance(point1, point2) - error
    equation, (A, B, C, D) = plane

    m = x2 - x1
    n = y2 - y1
    p = z2 - z1

    if A * m + B * n + C * p == 0: return None

    t = -(A * x1 + B * y1 + C * z1 + D) / (A * m + B * n + C * p)

    x = x1 + m * t
    y = y1 + n * t
    z = z1 + p * t

    point = (x, y, z)

    if distance(point, point1) > dist or distance(point, point2) > dist:
        return None

    if accessory(point, facet) and point != point1: return point
    else: return None


# Builds flat equation for given points
#
def plane(points):
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]

    A = (y2 - y1) * (z3 - z1) - (y3 - y1) * (z2 - z1)
    B = (x3 - x1) * (z2 - z1) - (x2 - x1) * (z3 - z1)
    C = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    D = -(A * x1 + B * y1 + C * z1)

    # Equation to determine whether point belongs to plane
    #
    def equation(point):
        x, y, z = point
        expression = x * A + y * B + z * C + D
        return expression == 0

    return equation, (A, B, C, D)

# Determine whether point belongs to facet
#
def accessory(point, facet):
    x, y, z = point
    s = 0

    for i in range(len(facet) - 1):
        s += square(point, facet[i], facet[i + 1])

    s += square(point, facet[-1], facet[0])

    return s <= polygonSquare(facet) + error

# Square of polygon
#
def polygonSquare(facet):
    s = 0
    point = facet[0]

    for i in range(1, len(facet) - 1):
        s += square(point, facet[i], facet[i + 1])

    return s

# Square of triangle
#
def square(point1, point2, point3):
    a = distance(point1, point2)
    b = distance(point2, point3)
    c = distance(point1, point3)

    p = (a + b + c) / 2

    return math.sqrt(abs((p * (p - a) * (p - b) * (p - c))))

# Distance between two points
#
def distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    d = sqr(x2 - x1) + sqr(y2 - y1) + sqr(z2 - z1)

    return math.sqrt(d)

# Cosinus of angle between line and plane
#
def cosLinePlaneAngle(point1, point2, normal):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    A, B, C, D = normal

    m = x2 - x1
    n = y2 - y1
    p = z2 - z1

    len1 = math.sqrt(sqr(A) + sqr(B) + sqr(C))
    len2 = math.sqrt(sqr(m) + sqr(n) + sqr(p))

    return abs(A * m + B * n + C * p) / (len1 * len2)
