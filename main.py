
import parserObj
import tracing as tr
import geometry as geom
import KDTree
import output

vertices, facets = parserObj.getObjectConfig('./objects/cow.obj')

cameraPos = (0, -2, 0)
lightPos = (0, 1, -1)
size = (720, 720)
distance = 1

imagePlane = tr.buildImagePlane(size, cameraPos, distance)
normals = [geom.plane(facet) for facet in facets]
tree = KDTree.buildTree(facets, normals)

image = tr.render(cameraPos, lightPos, imagePlane, facets, tree)
output.writeToBMP(image, size, 'images/cow.bmp')
