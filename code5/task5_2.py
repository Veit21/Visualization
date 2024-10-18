import vtk # the visualization toolkit

# Data structures for point field
gridSize = 16
points = vtk.vtkPoints()

# Create point geometry (the coordinates)
for i in range(gridSize):
    for j in range(gridSize):
        # calculate coordinates
        x = i / (gridSize - 1.0) * 3.0 - 1.0
        y = j / (gridSize - 1.0) * 3.0 - 2.0
        z = x * x**2 / 3.0 + y * y**2 / 3.0 - x * x / 2.0 + y * y / 2.0
        
        # insert the point (geometry)
        points.InsertNextPoint(x, y, z)


polydata = vtk.vtkPolyData()
polydata.SetPoints(points)

# initializing a vertex glyph filter
vertexFilter = vtk.vtkVertexGlyphFilter()
vertexFilter.SetInputData(polydata)
vertexFilter.Update()

# initializing a delaunay filter
delaunayFilter = vtk.vtkDelaunay2D()
delaunayFilter.SetInputData(polydata)
delaunayFilter.Update()

# mapper for the vertex glyph filter
vertexFilterMapper = vtk.vtkPolyDataMapper()
vertexFilterMapper.SetInputConnection(vertexFilter.GetOutputPort())

# mapper for the delaunay filter
delaunayFilterMapper = vtk.vtkPolyDataMapper()
delaunayFilterMapper.SetInputConnection(delaunayFilter.GetOutputPort())

# actor for the vertex glyph mapper
vertexFilterActor = vtk.vtkActor()
vertexFilterActor.SetMapper(vertexFilterMapper)
vertexFilterActor.GetProperty().SetPointSize(8)
vertexFilterActor.GetProperty().SetRenderPointsAsSpheres(True)
vertexFilterActor.GetProperty().SetColor(1.0, 0.0, 0.0)

# actor for the delaunay mapper
delaunayFilterActor = vtk.vtkActor()
delaunayFilterActor.SetMapper(delaunayFilterMapper)
delaunayFilterActor.GetProperty().SetEdgeVisibility(True)


renderer = vtk.vtkRenderer()
renderer.AddActor(vertexFilterActor)
renderer.AddActor(delaunayFilterActor)
renderer.SetBackground(0.8, 0.8, 0.8)

renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderWindowInteractor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

renderWindowInteractor.Start()
