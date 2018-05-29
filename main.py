import parserObj
import tracing as tr
import geometry as geom

vertices, normals, facets = parserObj.getObjectConfig('./objects/triangle.obj')

cameraPos = (0, 0, 0)
size = (24, 24)
distance = 12

imagePlane = tr.buildImagePlane(size, cameraPos, distance)
equations = [geom.plane(facet) for facet in facets]

img = tr.render(cameraPos, imagePlane, equations, facets)

for row in img:
    print(row)
