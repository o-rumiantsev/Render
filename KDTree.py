from geometry import centroid, intersection, rayBoxIntersection
import pprint

pp = pprint.PrettyPrinter(indent = 1)

DIMENSIONS = 3

def buildTree(facets, normals):
    for i in range(len(facets)):
        facets[i] = {
            'triangle': facets[i],
            'normal': normals[i]
        }

    return build(facets)


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
    left = ordered[:int(n / 2)]
    right = ordered[int(n / 2 + 1):]
    splitPoint = ordered[int(n / 2)]
    minPoint, maxPoint = boundingBox(facets)

    node = {
        'min': minPoint,
        'max': maxPoint,
        'split': splitPoint
    }

    if n == 1:
        return node

    node['left'] = _build(left, depth + 1)
    node['right'] = _build(right, depth + 1)

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

def findIntersection(point1, point2, tree):
    intersect = rayBoxIntersection(
        point1, point2, (tree['min'], tree['max'])
    )

    if intersect == float('inf'): return float('inf'), None

    if not 'left' in tree and not 'right' in tree:
        facet = tree['split']
        distance = intersection(point1, point2, facet['triangle'])
        return distance, facet

    triangle = tree['split']['triangle']
    distance = intersection(point1, point2, triangle)

    intersectLeft = float('inf')
    intersectRight = float('inf')

    if tree['left'] != None:
        intersectLeft = rayBoxIntersection(
            point1, point2, (tree['left']['min'], tree['left']['max'])
        )

    if tree['right'] != None:
        intersectRight = rayBoxIntersection(
            point1, point2, (tree['right']['min'], tree['right']['max'])
        )

    closest = {
        'dist': float('inf'),
        'dir': None
    }

    further = {
        'dist': float('inf'),
        'dir': None
    }

    if intersectLeft > intersectRight:
        closest['dist'] = intersectRight
        further['dist'] = intersectLeft
        closest['dir'] = 'right'
        further['dir'] = 'left'
    else:
        closest['dist'] = intersectLeft
        further['dist'] = intersectRight
        closest['dir'] = 'left'
        further['dir'] = 'right'

    distC, triangleC = float('inf'), ()
    distF, triangleF = float('inf'), ()

    if closest['dist'] != float('inf'):
        distC, triangleC = findIntersection(point1, point2, tree[closest['dir']])
        if distC == float('inf') and further['dist'] != float('inf'):
            distF, triangleF = findIntersection(point1, point2, tree[further['dir']])

    distances = [
        (distance, tree['split']),
        (distC, triangleC),
        (distF, triangleF)
    ]

    return min(distances, key = lambda x: x[0])
