import parserObj
import tracing as tr
import geometry as geom
import KDTree
import output

vertices, normals, facets = parserObj.getObjectConfig('./objects/cube.obj')

cameraPos = (0, 0, 0)
size = (512, 512)
distance = 256

imagePlane = tr.buildImagePlane(size, cameraPos, distance)
equations = [geom.plane(facet) for facet in facets]

image = tr.render(cameraPos, imagePlane, equations, facets)
output.writeToBMP(image, size, 'img.bmp')
#
# verticesKDTree = KDTree.build(vertices, 3)
# best = KDTree.closestPoint(verticesKDTree, (-2, 2, 0), 3)
#
# print(verticesKDTree)
# print(best)
