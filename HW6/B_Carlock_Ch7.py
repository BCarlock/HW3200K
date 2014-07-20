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


#Still working on it
import arcpy
from arcpy import env
env.workspace = "E:/Python_Prog/Python/Data/Exercise07/roads.shp"
fc = "roads.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldfeature = arcpy.ValidateFieldName(newfield)
cursor = arcpy.AddField_management("roads", "Ferry", "TEXT", 3)

arcpy.AddField_management(fc, "FERRY", "TEXT","","", "")
delimfield1 = arcpy.AddFieldDelimiters(fc, "FERRY")
delimfield2 = arcpy.AddFieldDelimiters(fc, "FEATURE")
cursor = arcpy.da.UpdateCursor(fc,["FEATURE", "FERRY"])
for row in cursor:
  if row[0] == 'Ferry Crossing':
    row[1] = 'YES'
  else:
    row[1] = 'NO'
    cursor.updateRow(row)

del row
del cursor
del fc
