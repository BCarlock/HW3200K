## EXE 6
## Challenge Question 1:

import arcpy
from arcpy import env
env.workspace = "C:/Data"
fieldlist = arcpy.ListFields()
for field in fieldlist:
    print (field.name + " is a " + field.type)
    

## Challenge Question 2
    
import arcpy
from arcpy import env
env.workspace = "C:/Data"
polylist = arcpy.ListRasters("", "polygon")
for poly in polylist:
    arcpy.BuildPyramids_managment(polygon)
    print polylist
