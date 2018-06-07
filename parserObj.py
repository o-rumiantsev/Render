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

def getNormals(lines):
    normals = []

    for line in lines:
        if not len(line): continue

        if line[0] == 'vn':
            line = [float(value) for value in line[1:]]
            normal = tuple(line)
            normals.append(normal)

    return normals

def getFacets(lines):
    facets = []

    for line in lines:
        if not len(line): continue

        if line[0] == 'f':
            vertices = [int(value.split('/')[0]) for value in line[1:]]
            normals = [int(value.split('/')[2]) for value in line[1:]]
            facet = (tuple(vertices), tuple(normals))
            facets.append(facet)

    return facets

def prepareFacets(vertices, normals, facets):
    preparedFacets = []

    for facet in facets:
        preparedVertices = [vertices[index - 1] for index in facet[0]]
        preparedNormals = [normals[index - 1] for index in facet[1]]
        prepareFacet = {
            'triangle': preparedVertices,
            'normal': gm.avarageNormal(preparedNormals)
        }
        preparedFacets.append(prepareFacet)

    return preparedFacets


def getObjectConfig(filename, normalizator = False):
    configFile = open(filename, 'r');
    lines = [line.strip().split() for line in configFile]
    configFile.close()

    vertices = getVertices(lines)
    normals = getNormals(lines)

    if normalizator:
    #     vertices = normalize(vertices)
        normals = normalize(normals)
        
    facets = prepareFacets(vertices, normals, getFacets(lines))

    return facets
