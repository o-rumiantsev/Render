import parserObj
import tracing as tr
import geometry as geom
import output

vertices, normals, facets = parserObj.getObjectConfig('./objects/cube.obj')

cameraPos = (0, 0, 0)
lightPos = (-100, 0, 500)
size = (800, 600)
distance = 400

imagePlane = tr.buildImagePlane(size, cameraPos, distance)
equations = [geom.plane(facet) for facet in facets]

image = tr.render(cameraPos, lightPos, imagePlane, equations, facets)
output.writeToBMP(image, size, 'cube.bmp')
