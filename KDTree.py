import geometry as geom

DIMENSION = 3

def build(triangles):
    for i in range(len(triangles)):
       triangles[i].append(geom.centroid(triangles[i]))

    tree = _build(triangles)

    return tree

def _build(triangles, depth = 0):
    n  = len(triangles)

    if n <= 0:
        return

    axis = depth % DIMENSION
    ordered = sorted(triangles, key = lambda centre: centre[3][axis])
    splitPoint = ordered[int(n / 2)]
    minPoint, maxPoint = boundingBox(triangles)

    node = {
        'min': minPoint,
        'max': maxPoint,
        'triangle': splitPoint
    }

    if n == 1:
        return node

    node['left'] = _build(ordered[:int(n / 2)], depth + 1)
    node['right'] = _build(ordered[int(n / 2 + 1):], depth + 1)

    return node

def boundingBox(triangles):
    xSorted = list(map(lambda triangle:
        sorted(triangle, key = lambda point: point[0]), triangles))
    ySorted = list(map(lambda triangle:
        sorted(triangle, key = lambda point: point[1]), triangles))
    zSorted = list(map(lambda triangle:
        sorted(triangle, key = lambda point: point[2]), triangles))

    xmin = min(xSorted, key = lambda point: point[0][0])[0][0]
    ymin = min(ySorted, key = lambda point: point[0][1])[0][1]
    zmin = min(zSorted, key = lambda point: point[0][2])[0][2]
    xmax = max(xSorted, key = lambda point: point[3][0])[3][0]
    ymax = max(ySorted, key = lambda point: point[3][1])[3][1]
    zmax = max(zSorted, key = lambda point: point[3][2])[3][2]

    return (xmin, ymin, zmin), (xmax, ymax, zmax)
