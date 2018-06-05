import geometry as gm

def normalize(vertices):
    maxLenVertex = max(vertices, key = lambda v: gm.vectorLength(v))
    maxLen = gm.vectorLength(maxLenVertex)

    return list(map(
        lambda v: (v[0] / maxLen, v[1] / maxLen, v[2] / maxLen), vertices
    ))


def getVertices(lines):
    vertices = []

    for line in lines:
        if not len(line): continue

        if line[0] == 'v':
            line = [float(value) for value in line[1:]]
            vertex = tuple(line)
            vertices.append(vertex)

    return vertices

def getFacets(lines):
    facets = []

    for line in lines:
        if not len(line): continue

        if line[0] == 'f':
            line = [int(value.split('/')[0]) for value in line[1:]]
            facet = tuple(line)
            facets.append(facet)

    return facets

def prepareFacets(vertices, facets):
    preparedFacets = []

    for facet in facets:
        prepared = [vertices[index - 1] for index in facet]
        preparedFacets.append(prepared)

    return preparedFacets


def getObjectConfig(filename, normalizator = False):
    configFile = open(filename, 'r');
    lines = [line.strip().split() for line in configFile]
    configFile.close()

    vertices = getVertices(lines)

    if normalizator:
        vertices = normalize(vertices)

    facets = prepareFacets(vertices, getFacets(lines))

    return vertices, facets
