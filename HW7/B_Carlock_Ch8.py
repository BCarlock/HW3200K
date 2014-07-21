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
import arcpy
from arcpy import env
env.workspace = "P:/Python Class/Python/Data/Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@"])
length = 0

for row in cursor:
    partnum = 0
    length = 0
    for part in row[0]:
        poly = arcpy.Polygon(part)
        print("Part {0} area: {1}".format(partnum, poly.area))
        print("Part {0} perimeter: {1}".format(partnum, poly.length))

        partnum += 1



# Challenge 3
