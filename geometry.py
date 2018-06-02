import math

sqr = lambda x: math.pow(x, 2)
epsilon = 1e-8

def vector(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    vec = (x2 - x1, y2 - y1, z2 - z1)

    return vec

# [Vector1 x Vector2]
#
def crossProduct(vec1, vec2):
    x = vec1[1] * vec2[2] - vec1[2] * vec2[1]
    y = vec1[2] * vec2[0] - vec1[0] * vec2[2]
    z = vec1[0] * vec2[1] - vec1[1] * vec2[0]
    return (x, y, z)

# (Vector1 * Vector2)
#
def dotProduct(vec1, vec2):
    x = vec1[0] * vec2[0]
    y = vec1[1] * vec2[1]
    z = vec1[2] * vec2[2]
    return x + y + z

# Find point of intersection
#
def intersection(point1, point2, facet):
    origin = point1
    direction = vector(point1, point2)

    edge1 = vector(facet[0], facet[1])
    edge2 = vector(facet[0], facet[2])

    pvec = crossProduct(direction, edge2)
    det = dotProduct(edge1, pvec)

    if det < epsilon and det > -epsilon:
        return float('inf')

    tvec = vector(facet[0], origin)
    u = dotProduct(tvec, pvec) / det

    if u < 0 or u > 1:
        return float('inf')

    qvec = crossProduct(tvec, edge1)
    v = dotProduct(direction, qvec) / det

    if v < 0 or u + v > 1:
        return float('inf')

    distance = dotProduct(edge2, qvec) / det
    return distance


def lightIntersection(lightPos, vertices, facet):
    point1 = vertices[0]
    point2 = lightPos

    return intersection(point1, point2, facet)

def plane(points):
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]

    A = (y2 - y1) * (z3 - z1) - (y3 - y1) * (z2 - z1)
    B = (x3 - x1) * (z2 - z1) - (x2 - x1) * (z3 - z1)
    C = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    D = -(A * x1 + B * y1 + C * z1)

    return A, B, C, D

# Cosinus of angle between line and plane
#
def cosLinePlaneAngle(facet, normal, lightPos):
    x1, y1, z1 = facet[0]
    x2, y2, z2 = lightPos

    A, B, C, D = normal

    m = x2 - x1
    n = y2 - y1
    p = z2 - z1

    len1 = math.sqrt(sqr(A) + sqr(B) + sqr(C))
    len2 = math.sqrt(sqr(m) + sqr(n) + sqr(p))

    return abs(A * m + B * n + C * p) / (len1 * len2)

# Intersection between ray and box
#
def rayBoxIntersection(point1, point2, box):
    minPoint = box[0]
    maxPoint = box[1]

    facets = getTrianglesFromBox(minPoint, maxPoint)
    closest = min([intersection(point1, point2, facet) for facet in facets])

    return closest != float('inf')

def getTrianglesFromBox(minPoint, maxPoint):
    x0, y0, z0 = minPoint
    x1, y1, z1 = maxPoint

    v1 = minPoint
    v2 = (x0, y0, z1)
    v3 = (x0, y1, z1)
    v4 = (x0, y1, z0)
    v5 = (x1, y0, z0)
    v6 = (x1, y0, z1)
    v7 = maxPoint
    v8 = (x1, y1, z0)

    triangles = [
        (v1, v2, v3),
        (v1, v4, v3),
        (v1, v5, v6),
        (v1, v6, v2),
        (v1, v4, v8),
        (v1, v8, v5),
        (v2, v3, v7),
        (v2, v7, v6),
        (v5, v6, v7),
        (v5, v7, v8)
    ]

    return triangles
