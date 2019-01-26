#!/usr/bin/pvpython


from paraview.simple import *

import time
def generate_image(filename):
	reader = XMLUnstructuredGridReader(FileName=filename)


	Show(reader)
	Render()
	ai = reader.PointData[1]
	dp = GetDisplayProperties(reader)
	print(ai.GetRange())
	# To color the representation by an array, we need to first create
	# a lookup table.  We use the range of the Elevation array
	dp.LookupTable = MakeBlueToRedLT(ai.GetRange()[0], ai.GetRange()[1])
	dp.ColorArrayName = ("POINTS", "Real part")
	Render()

	#save screenshot
	print(filename)
	WriteImage(filename+"_img.png")

