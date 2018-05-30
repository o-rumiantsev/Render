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

def render(cameraPos, imagePlane, equations, facets):
    image = []
    for row in imagePlane:
        pixelRow = []
        for pixel in row:
            bit = findIntersections(cameraPos, pixel, equations, facets)
            pixelRow.append(bit)

        image.append(pixelRow)

    return image

def findIntersections(cameraPos, pixel, equations, facets):
    minDistance = float('inf')

    for i in range(len(facets)):
        point = geom.intersection(cameraPos, pixel, equations[i], facets[i])
        if not point: continue
        d = geom.distance(cameraPos, point)
        if d < minDistance: minDistance = d

    if minDistance == float('inf'): return 255
    else: return 0
