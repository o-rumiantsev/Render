# def intersection(point1, point2, flat):


# Builds flat equation for given points
#
def flat(points):
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]

    A = (y2 - y1) * (z3 - z1) - (y3 - y1) * (z2 - z1)
    B = (x3 - x1) * (z2 - z1) - (x2 - x1) * (z3 - z1)
    C = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    # Equation to determine whether point belongs to flat
    #
    def equation(point):
        x, y, z = point
        expression = (x - x1) * A + (y - y1) * B + (z - z1) * C
        return expression == 0

    return equation
