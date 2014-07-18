# Chapter 7 Question 1
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
fc = "airports.shp"
seaplane = 'Seaplane Base'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" =\'Seaplane Base\'')
for row in cursor:
    arcpy.Buffer_analysis("Seaplane Base", "Seaplane Buffer", "7500 METERS", )
    


import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
fc = "airports.shp"
airport = 'airports'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" =\'airports\'')
for row in cursor:
    arcpy.Buffer_analysis("airports", "Airport Buffer", "15000 METERS", )
    
    
#or
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
fc = "airports.shp"
airport = 'airports'
seaplane = 'Seaplane Base'
cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" =\'airports\'')
for row in cursor:
    arcpy.Buffer_analysis("airports", "Airport Buffer", "15000 METERS", )
cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" =\'Seaplane Base\'')
for row in cursor:
    arcpy.Buffer_analysis("Seaplane Base", "Seaplane Buffer", "7500 METERS", )



# Chapter 7 Question 2
import arcpy
from arcpy import env
env.workspace = "E:/Python/Homework/Data/Exercise07/Roads.shp"
fc = "Results/Roads.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldfeature = arcpy.ValidateFieldName(newfield)
cursor = arcpy.AddField_management("roads", "Ferry", "TEXT", 3)
