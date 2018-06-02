import geometry as geom

def buildImagePlane(size, cameraPos, distance):
    xmax = size[0] / 2
    zmax = size[1] / 2

    y = cameraPos[1] + distance
    z = size[1] / 2

    imagePlane = []

    for i in range(size[1] + 1):
        x = -size[0] / 2
        imagePlane.append([])
        for j in range(size[0] + 1):
            imagePlane[i].append((x / xmax, y, z / zmax))
            x += 1

        z -= 1

    return imagePlane

def render(cameraPos, lightPos, imagePlane, normals, facets):
    image = [[colorify(cameraPos, pixel, lightPos, normals, facets)
                for pixel in row]
                    for row in imagePlane]

    return image

def colorify(cameraPos, pixel, lightPos, normals, facets):
    facet, normal = findIntersections(cameraPos, pixel, normals, facets)
    bit = 255

    if facet:
        bit = buildShadow(lightPos, facet, normal, facets)

    return bit

def findIntersections(cameraPos, pixel, normals, facets):
    distance = min([(geom.intersection(cameraPos, pixel, facets[i]), i)
                    for i in range(len(facets))], key = lambda x: x[0])

    index = distance[1]
    distance = distance[0]

    if distance == float('inf'): return None, None
    else: return facets[index], normals[index]


shadowCache = {}
def buildShadow(lightPos, facet, normal, facets):
    global shadowCache

    key = str([lightPos, facet, normal])
    if key in shadowCache:
        return shadowCache[key]

    shadowed = 50
    light = 200

    for i in range(len(facets)):
        if facet == facets[i]: continue
        if geom.lightIntersection(lightPos, facet, facets[i]):
            shadowCache[key] = shadowed
            return shadowed

    shadowCoeficient = geom.cosLinePlaneAngle(facet, normal, lightPos)
    shadowness = abs(shadowCoeficient) * light
    shadowCache[key] = shadowness
    return shadowness
