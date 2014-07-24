# Challenge 1
import arcpy
mxd = arcpy.mapping.MapDocument("E:\Python Class\Python\Data\Exercise10\Austin_TX.mxd")
dfs = arcpy.mapping.ListDataFrames(mxd)
addLayer = arcpy.mapping.ListLayers(mxd, "parks")[0]
for df in dfs:
  print df, df.name
  if df.name != "Parks":
     df2 = arcpy.mapping.ListDataFrames(mxd, df.name)[0]
     print df2
     arcpy.mapping.AddLayer(df2, addLayer, "BOTTOM")
      
mxd.saveACopy("E:\Python Class\Python\Data\Exercise10\Results\Austin_TX_2.mxd")

del mxd
del addLayer


import arcpy
