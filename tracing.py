from geometry import intersection, lightIntersection, cosLinePlaneAngle
from KDTree import findIntersection

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

def render(cameraPos, lightPos, imagePlane, facets, tree):
    image = [[colorify(cameraPos, pixel, lightPos, facets, tree)
                for pixel in row]
                    for row in imagePlane]

    return image

def colorify(cameraPos, pixel, lightPos, facets, tree):
    facet, normal = findIntersections(cameraPos, pixel, tree)
    bit = 255

    if facet:
        bit = 0
    #     bit = buildShadow(lightPos, facet, normal, facets)

    return bit

def findIntersections(cameraPos, pixel, tree):
    distance, facet = findIntersection(cameraPos, pixel, tree)
    if distance == float('inf'): return None, None
    else: return facet['triangle'], facet['normal']


shadowCache = {}
def buildShadow(lightPos, facet, normal, facets):
    global shadowCache

    key = str([lightPos, facet, normal])
    if key in shadowCache:
        return shadowCache[key]

    shadowed = 50
    light = 200
    #
    # for i in range(len(facets)):
    #     if facet == facets[i]: continue
    #     distance = lightIntersection(lightPos, facet, facets[i])
    #     print(distance)
    #     if distance == float('inf') or distance == 0:
    #         shadowCache[key] = shadowed
    #         return shadowed

    shadowCoeficient = cosLinePlaneAngle(facet, normal, lightPos)
    shader = abs(shadowCoeficient) * light
    shadowCache[key] = shader
    return shader
