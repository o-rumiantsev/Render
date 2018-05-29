import parserObj
import tracing as tr
import geometry as geom

vertices, normals, flats = parserObj.getObjectConfig('./objects/cube.obj')

cameraPos = (0, 0, 0)
size = (24, 24)
distance = 12

imagePlane = tr.buildImagePlane(size, cameraPos, distance)

equations = [geom.flat(flat) for flat in flats]
geom.intersection(cameraPos, (0, 12, 0), equations[0]) # (0, 14, 0) for cube.obj
