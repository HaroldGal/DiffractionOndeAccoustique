# -*- coding: utf-8 -*-
import numpy as np
def createVisu(X, posPoints, triangles): # X champ scalaire
	file = open("out.vtu","w")
	file.write('<VTKFile type="UnstructuredGrid" version="1.0" byte_order="LittleEndian" header_type="UInt64">\n')
	file.write("<UnstructuredGrid>\n")
	file.write('<Piece NumberOfPoints="' + str(len(posPoints))+'" NumberOfCells="'+str(len(triangles))+'">\n')
	file.write("<Points>\n")
	file.write('<DataArray NumberOfComponents="3" type="Float64">\n')
	for i in posPoints:
		for j in i:
			file.write(str(j) + ' ')
		file.write('\n')

	file.write('</DataArray>\n</Points>\n<Cells>\n<DataArray type="Int32" Name="connectivity">\n')

	for i in triangles:
		for j in i:
			file.write(str(j) + ' ')
		file.write('\n')

	file.write('</DataArray>\n<DataArray type="Int32" Name="offsets">\n')

	for i in range(len(triangles)):
		file.write(str((i+1)*3) + '\n')

	file.write('</DataArray>\n<DataArray type="UInt8" Name="types">\n')

	for i in range(len(triangles)):
		file.write('5\n')

	file.write('</DataArray>\n</Cells>\n<PointData Scalars="solution">\n<DataArray type="Float64" Name="Real part" format="ascii">\n')
	for i in X:
		file.write(str(np.real(i)) + "\n")
	file.write('</DataArray>\n')
	file.write('<DataArray type="Float64" Name="Imag part" format="ascii">\n')
	for i in X:
		file.write(str(np.imag(i)) + "\n")
	file.write('</DataArray>\n')

	file.write('</PointData>\n</Piece>\n</UnstructuredGrid>\n</VTKFile>\n')
	file.close()