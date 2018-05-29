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
    for line in lines:
        if not len(line): continue

        if line[0] == 'vn':
            print(line)

def getFlats(lines):
    flats = []

    for line in lines:
        if not len(line): continue

        if line[0] == 'f':
            line = [int(value) for value in line[1:]]
            flat = tuple(line)
            flats.append(flat)

    return flats

def prepareFlats(vertices, flats):
    preparedFlats = []

    for flat in flats:
        prepared = [vertices[index - 1] for index in flat]
        preparedFlats.append(prepared)

    return preparedFlats


def getObjectConfig(filename):
    configFile = open(filename, 'r');
    lines = [line.strip().split() for line in configFile]
    configFile.close()

    vertices = getVertices(lines)
    normals = getNormals(lines)
    flats = prepareFlats(vertices, getFlats(lines))

    return vertices, normals, flats
