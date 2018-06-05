import parserObj
import tracing as tr
import geometry as geom
import KDTree
import output
from time import time

start = time()
vertices, facets = parserObj.getObjectConfig('./objects/dolphin.obj', True)

cameraPos = (0, 0, 1)
direction = (0, 0, -1)
lightPos = (0, 0, 10)
size = (1024, 1024)
distance = 1

imagePlane = tr.buildImagePlane(size, cameraPos, direction, distance)
normals = [geom.plane(facet) for facet in facets]
tree = KDTree.buildTree(facets, normals)
print(tree['min'], tree['max'])
image = tr.render(cameraPos, lightPos, imagePlane, facets, tree)
print(time() - start)

output.writeToBMP(image, size, 'images/dolphin.bmp')
