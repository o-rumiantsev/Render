import parserObj
import tracing as tr
import geometry as geom
import KDTree
import output
from time import time

start = time()
facets = parserObj.getObjectConfig('./objects/cow.obj', True)

cameraPos = (0.25, -1, 0.3)
direction = (0, 1, 0)
lightPos = (10, -10, 10)
size = (1024, 1024)
distance = 1

imagePlane = tr.buildImagePlane(size, cameraPos, direction, distance)
tree = KDTree.buildTree(facets)

image = tr.render(cameraPos, lightPos, imagePlane, tree)
print(time() - start)

output.writeToBMP(image, size, 'images/cow.rgb.bmp')
