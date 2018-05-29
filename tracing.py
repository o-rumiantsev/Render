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
