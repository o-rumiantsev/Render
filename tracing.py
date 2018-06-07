import geometry as gm
from KDTree import findIntersection

def buildImagePlane(size, cameraPos, direction, distance):
    viewVector = gm.multiplyVector(direction, distance)
    imPos = gm.vectorSum(cameraPos, viewVector)

    const = tuple(filter(lambda x: x != 0, viewVector))[0]
    const = viewVector.index(const)

    pixel = [0, 0, 0]
    pixel[const] = imPos[const]

    [colCoord, rowCoord] = [i for i, c in enumerate(viewVector) if c == 0]

    colMax = size[0] / 2
    rowMax = size[1] / 2


    imagePlane = []
    row = rowMax

    for i in range(size[1]):
        col = -colMax
        pixel[rowCoord] = row / rowMax + cameraPos[rowCoord]
        imagePlane.append([])
        for j in range(size[0]):
            pixel[colCoord] = col / colMax + cameraPos[colCoord]
            imagePlane[i].append(tuple(pixel))
            col += 1

        row -= 1

    return imagePlane

def render(cameraPos, lightPos, imagePlane, tree):
    image = [[colorify(cameraPos, pixel, lightPos, tree)
                for pixel in row]
                    for row in imagePlane]

    return image

def colorify(cameraPos, pixel, lightPos, tree):
    px = 255
    light = 200

    facet, normal = findIntersections(cameraPos, pixel, tree)

    if facet:
        color = gm.multiplyVector(gm.vectorSum(normal, gm.ones()), 0.5)
        px = gm.multiplyVector(color, 255)
        # px = buildShadow(lightPos, facet, normal, tree)

    return px

def findIntersections(point1, point2, tree):
    distance, facet = findIntersection(point1, point2, tree)
    if distance == float('inf'): return None, None
    else: return facet['triangle'], facet['normal']


shadowCache = {}
def buildShadow(lightPos, facet, normal, tree):
    global shadowCache

    key = str([lightPos, facet, normal])
    if key in shadowCache:
        return shadowCache[key]

    shadowed = 10
    light = 200

    centroid = facet[3]

    obstacle, obsNormal = findIntersections(lightPos, centroid, tree)
    if obstacle and obstacle != facet:
        shadowCache[key] = shadowed
        return shadowed


    shadowCoeficient = gm.cosLinePlaneAngle(lightPos, centroid, normal)
    shader = abs(shadowCoeficient) * light
    shadowCache[key] = shader
    return shader
