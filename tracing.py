import geometry as geom

def buildImagePlane(size, cameraPos, distance):
    y = cameraPos[1] + distance
    z = size[1]/2

    imagePlane = []

    for i in range(size[1] + 1):
        x = -size[0]/2
        imagePlane.append([])
        for j in range(size[0] + 1):
            imagePlane[i].append((x, y, z))
            x += 1

        z -= 1

    return imagePlane

def render(cameraPos, lightPos, imagePlane, equations, facets):
    image = []
    for row in imagePlane:
        pixelRow = []
        for pixel in row:
            point, normal = findIntersections(cameraPos, pixel, equations, facets)
            bit = 255

            if point:
                bit = buildShadow(point, lightPos, normal, equations, facets)

            pixelRow.append(bit)

        image.append(pixelRow)

    return image

def findIntersections(cameraPos, pixel, equations, facets):
    minDistance = float('inf')
    intersectionPoint = ()
    normal = ()

    for i in range(len(facets)):
        point = geom.intersection(cameraPos, pixel, equations[i], facets[i])
        if not point: continue
        d = geom.distance(cameraPos, point)
        if d < minDistance:
            minDistance = d
            intersectionPoint = point
            normal = equations[i][1]

    if minDistance == float('inf'): return None, None
    else: return intersectionPoint, normal

def buildShadow(point, lightPos, normal, equations, facets):
    shadowed = 50
    light = 200

    for i in range(len(facets)):
        if geom.lightIntersection(point, lightPos, equations[i], facets[i]):
            return shadowed

    shadowCoeficient = geom.cosLinePlaneAngle(point, lightPos, normal)
    return shadowCoeficient * light
