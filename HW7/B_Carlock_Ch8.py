#Challenge 1
import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "P:/Python Class/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "P:/Python Class/Python/Data/Exercise08"
newfc = "Results/square.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
infile = "P:/Python Class/Python/Data/Exercise08/Results/square.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line, " ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
fileinput.close()
del cursor



# Challenge 2




# Challenge 3
