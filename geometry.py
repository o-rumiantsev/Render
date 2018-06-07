import math

sqr = lambda x: math.pow(x, 2)
epsilon = 1e-8

# |Vector|
#
def vectorLength(vector):
    x, y, z = vector
    return math.sqrt(sqr(x) + sqr(y) + sqr(z))

# x^2 + y^2 + z^2 = 1
#
def normalizeVector(vector):
    x, y, z = vector
    len = vectorLength(vector)
    return (x / len, y / len, z / len)

def vector(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    vec = (x2 - x1, y2 - y1, z2 - z1)

    return vec

# Vector1 + Vector2
#
def vectorSum(vec1, vec2):
    x = vec1[0] + vec2[0]
    y = vec1[1] + vec2[1]
    z = vec1[2] + vec2[2]
    return (x, y, z)

# Vector * Number
#
def multiplyVector(vector, number):
    return tuple(map(lambda v: v * number, vector))

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


# Centre of triangle
#
def centroid(points):
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]

    xCentre = (x1 + x2 + x3) / 3
    yCentre = (y1 + y2 + y3) / 3
    zCentre = (z1 + z2 + z3) / 3

    return xCentre, yCentre, zCentre

# Compute avarage normal direction
#
def avarageNormal(normals):
    norm1, norm2, norm3 = normals
    normal = vectorSum(norm1, norm2)
    normal = vectorSum(normal, norm3)
    return normalizeVector(normal)

# Distance between two points
#
def distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    d = sqr(x2 - x1) + sqr(y2 - y1) + sqr(z2 - z1)

    return math.sqrt(d)

# Cosinus of angle between line and plane
#
def cosLinePlaneAngle(lightPos, centroid, normal):
    A, B, C, D = normal

    m, n, p = vector(lightPos, centroid)

    len1 = math.sqrt(sqr(A) + sqr(B) + sqr(C))
    len2 = math.sqrt(sqr(m) + sqr(n) + sqr(p))
    cos = abs(A * m + B * n + C * p) / (len1 * len2)

    return cos

# Intersection between ray and box
#
def rayBoxIntersection(point1, point2, box):
    x0, y0, z0 = box[0]
    x1, y1, z1 = box[1]

    m, n, p = normalizeVector(vector(point1, point2))
    x, y, z = point1

    Tnear, Tfar = -float('inf'), float('inf')
    if m == 0:
        if x > x1 or x < x0:
            return float('inf')
    else:
        Tnear = (x0 - x) / m
        Tfar = (x1 - x) / m
        if Tnear > Tfar: Tfar, Tnear = Tnear, Tfar

    if n == 0:
        if y > y1 or y < y0:
            return float('inf')
    else:
        T1y = (y0 - y) / n
        T2y = (y1 - y) / n

        if T1y > T2y: T2y, T1y = T1y, T2y

        if T1y > Tnear: Tnear = T1y
        if T2y < Tfar: Tfar = T2y

    if Tnear > Tfar or Tfar < 0:
        return float('inf')

    if p == 0:
        if z > z1 or z < z0:
            return float('inf')
    else:
        T1z = (z0 - z) / p
        T2z = (z1 - z) / p

        if T1z > T2z: T2z, T1z = T1z, T2z

        if T1z > Tnear: Tnear = T1z
        if T2z < Tfar: Tfar = T2z

    if Tnear > Tfar or Tfar == 0:
        return float('inf')

    return Tnear
