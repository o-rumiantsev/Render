
import parserObj
import tracing as tr
import geometry as geom
import KDTree
import output
from time import time
import pprint

pp = pprint.PrettyPrinter(indent=1)

start = time()
vertices, facets = parserObj.getObjectConfig('./objects/triangle.obj')

cameraPos = (0, -2, 0)
lightPos = (0, 0, 3)
size = (64, 64)
distance = 1

imagePlane = tr.buildImagePlane(size, cameraPos, distance)
normals = [geom.plane(facet) for facet in facets]
tree = KDTree.buildTree(facets, normals)

# pp.pprint(tree)
image = tr.render(cameraPos, lightPos, imagePlane, facets, tree)
print(time() - start)

output.writeToBMP(image, size, 'triangle.bmp')
