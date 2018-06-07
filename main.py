import parserObj
import tracing as tr
import geometry as geom
import KDTree
import output
from time import time

start = time()
facets = parserObj.getObjectConfig('./objects/cow.obj', True)

cameraPos = (0, 1.5, 0)
direction = (0, -1, 0)
lightPos = (0, -2, 0)
size = (1024, 1024)
distance = 1

imagePlane = tr.buildImagePlane(size, cameraPos, direction, distance)
normals = [geom.plane(facet) for facet in facets]
tree = KDTree.buildTree(facets, normals)

image = tr.render(cameraPos, lightPos, imagePlane, tree)
print(time() - start)

output.writeToBMP(image, size, 'images/cow2.0.bmp')
