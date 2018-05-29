# Find point of intersection
#
def intersection(point1, point2, flat):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    equation, (A, B, C, D) = flat

    m = x2 - x1
    n = y2 - y1
    p = z2 - z1

    t = -(A * x1 + B * y1 + C * z1 + D) / (A * m + B * n + C * p)

    x = x1 + m * t
    y = y1 + n * t
    z = z1 + p * t

    return(x, y, z)

# Builds flat equation for given points
#
def flat(points):
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]

    A = (y2 - y1) * (z3 - z1) - (y3 - y1) * (z2 - z1)
    B = (x3 - x1) * (z2 - z1) - (x2 - x1) * (z3 - z1)
    C = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    D = -(A * x1 + B * y1 + C * z1)

    # Equation to determine whether point belongs to flat
    #
    def equation(point):
        x, y, z = point
        expression = x * A + y * B + z * C + D
        return expression == 0

    return equation, (A, B, C, D)
