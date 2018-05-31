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
            line = [int(value) for value in line[1:]]
            facet = tuple(line)
            facets.append(facet)

    return facets

def prepareFacets(vertices, facets):
    preparedFacets = []

    for facet in facets:
        prepared = [vertices[index - 1] for index in facet]
        preparedFacets.append(prepared)

    return preparedFacets


def getObjectConfig(filename):
    configFile = open(filename, 'r');
    lines = [line.strip().split() for line in configFile]
    configFile.close()

    vertices = getVertices(lines)
    facets = prepareFacets(vertices, getFacets(lines))

    return vertices, facets
