import parserObj
import tracing as tr
import geometry as geom
import KDTree
import output
from time import time

vertices, facets = parserObj.getObjectConfig('./objects/cow.obj')

cameraPos = (0, -2, 0)
lightPos = (0, 0, 1)
size = (600, 400)
distance = 1

tree = KDTree.build(facets)

imagePlane = tr.buildImagePlane(size, cameraPos, distance)
normals = [geom.plane(facet) for facet in facets]

image = tr.render(cameraPos, lightPos, imagePlane, normals, facets)
output.writeToBMP(image, size, 'cubek.bmp')
