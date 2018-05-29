import parserObj
import tracing as tr
import geometry as geom

vertices, normals, flats = parserObj.getObjectConfig('./objects/cube.obj')

cameraPos = (0, 0, 0)
size = (24, 24)
distance = 12

imagePlane = tr.buildImagePlane(size, cameraPos, distance)
