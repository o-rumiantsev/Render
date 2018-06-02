import parserObj
import tracing as tr
import geometry as geom
import KDTree
import output
from time import time

start = time()
vertices, facets = parserObj.getObjectConfig('./objects/cow.obj')

cameraPos = (0, -2, 0)
lightPos = (0, 0, 3)
size = (256, 256)
distance = 1

imagePlane = tr.buildImagePlane(size, cameraPos, distance)
normals = [geom.plane(facet) for facet in facets]

image = tr.render(cameraPos, lightPos, imagePlane, normals, facets)
print(time() - start)

output.writeToBMP(image, size, 'cow.bmp')
