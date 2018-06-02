from geometry import centroid, intersection, rayBoxIntersection

DIMENSIONS = 3

def build(facets):
    for i in range(len(facets)):
       facets[i]['triangle'].append(centroid(facets[i]['triangle']))

    tree = _build(facets)

    return tree

def _build(facets, depth = 0):
    n = len(facets)

    if n <= 0:
        return None

    axis = depth % DIMENSIONS
    ordered = sorted(facets, key = lambda f: f['triangle'][3][axis])
    splitPoint = ordered[int(n / 2)]
    minPoint, maxPoint = boundingBox(facets)

    node = {
        'min': minPoint,
        'max': maxPoint,
        'split': splitPoint
    }

    if n == 1:
        return node

    node['left'] = _build(ordered[:int(n / 2)], depth + 1)
    node['right'] = _build(ordered[int(n / 2 + 1):], depth + 1)

    return node

def boundingBox(facets):
    xSorted = list(map(lambda facet:
        sorted(facet['triangle'], key = lambda point: point[0]), facets))
    ySorted = list(map(lambda facet:
        sorted(facet['triangle'], key = lambda point: point[1]), facets))
    zSorted = list(map(lambda facet:
        sorted(facet['triangle'], key = lambda point: point[2]), facets))

    xmin = min(xSorted, key = lambda f: f[0][0])[0][0]
    ymin = min(ySorted, key = lambda f: f[0][1])[0][1]
    zmin = min(zSorted, key = lambda f: f[0][2])[0][2]
    xmax = max(xSorted, key = lambda f: f[3][0])[3][0]
    ymax = max(ySorted, key = lambda f: f[3][1])[3][1]
    zmax = max(zSorted, key = lambda f: f[3][2])[3][2]

    return (xmin, ymin, zmin), (xmax, ymax, zmax)

def findIntersection(point1, point2, tree, depth = 0):
    axis = depth % DIMENSIONS

    if tree is None:
        return float('inf'), None

    if not 'left' in tree and not 'right' in tree:
        facet = tree['split']
        distance = intersection(point1, point2, facet['triangle'])
        return distance, facet

    triangle = tree['split']['triangle']
    distance = intersection(point1, point2, triangle)

    if distance != float('inf'):
        return distance, tree['split']

    splitPoint1 = triangle[3]
    splitPoint2 = replaceValue(tree['min'], axis, splitPoint1[axis])
    splitPoint3 = replaceValue(tree['max'], axis, splitPoint1[axis])
    splitFacet = (splitPoint1, splitPoint2, splitPoint3)
    distanceToSplitFacet = intersection(point1, point2, splitFacet)

    intersectLeft = rayBoxIntersection(point1, point2, (tree['min'], splitPoint3))
    intersectRight = rayBoxIntersection(point1, point2, (tree['max'], splitPoint2))

    if distanceToSplitFacet != float('inf'):
        distanceL, triangleL = findIntersection(point1, point2, tree['left'], depth + 1)
        distanceR, triangleR = findIntersection(point1, point2, tree['right'], depth + 1)
        if distanceL < distanceR: return distanceL, triangleL
        else: return distanceR, triangleR

    if intersectLeft:
        return findIntersection(point1, point2, tree['left'], depth + 1)
    else:
        return findIntersection(point1, point2, tree['right'], depth + 1)

def replaceValue(immutable, index, value):
    changed = list(immutable)
    changed[index] = value
    return tuple(changed)
