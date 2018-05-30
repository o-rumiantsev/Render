import geometry as geom

def build(points, dimension, depth = 0):
    n  = len(points)

    if n <= 0:
        return None

    axis = depth % dimension
    sortedPoints = sorted(points, key = lambda point: point[axis])

    return {
        'point': sortedPoints[int(n / 2)],
        'left': build(sortedPoints[:int(n / 2)], depth + 1),
        'right': build(sortedPoints[int(n / 2 + 1):], depth + 1)
    }

def closer(currentPoint, point1, point2):
    if point1 is None:
        return point2

    if point2 is None:
        return point1

    distance1 = geom.distance(currentPoint, point1)
    distance2 = geom.distance(currentPoint, point2)

    return point1 if distance1 < distance2 else point2

def closestPoint(root, point, dimension, depth = 0):
    if root is None:
        return None

    axis = depth % dimension
    nextBranch = None
    oppositeBranch = None

    if point[axis] < root['point'][axis]:
        nextBranch = root['left']
        oppositeBranch = root['right']
    else:
        nextBranch = root['right']
        oppositeBranch = root['left']

    closest = closer(point, closestPoint(nextBranch, point, depth + 1), root['point'])

    if geom.distance(point, closest) > abs(point[axis] - root['point'][axis]):
        closest = closer(point, closestPoint(oppositeBranch, point, depth + 1), closest)

    return closest
