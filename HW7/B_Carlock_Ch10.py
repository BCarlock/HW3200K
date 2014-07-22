# Challenge 1
##import arcpy
##mxd = arcpy.mapping.MapDocument("E:\Python Class\Python\Data\Exercise10\Austin_TX.mxd")
##dfs = arcpy.mapping.ListDataFrames(mxd)
##addLayer = arcpy.mapping.ListLayers(mxd, "parks")[0]
##for df in dfs:
##  print df, df.name
##  if df.name != "Parks":
##     df2 = arcpy.mapping.ListDataFrames(mxd, df.name)[0]
##     print df2
##     arcpy.mapping.AddLayer(df2, addLayer, "BOTTOM")
##      
##  
##    
##    
##mxd.saveACopy("E:\Python Class\Python\Data\Exercise10\Results\Austin_TX_2.mxd")
##
##del mxd
##del addLayer


##import arcpy
##
###Reference layer in secondary map document
##mxd2 = arcpy.mapping.MapDocument(r"E:\Python Class\Python\Data\Exercise10\Austin_TX.mxd")
##df2 = arcpy.mapping.ListDataFrames(mxd2, "parks")[0]
##addLayer = arcpy.mapping.ListLayers(mxd2, "parks", df2)[0]
##
###Add layer into primary map document
##mxd = arcpy.mapping.MapDocument(r"E:\Python Class\Python\Data\Exercise10\Austin_TX.mxd")
##df = arcpy.mapping.ListDataFrames(mxd, "New Data Frame")[0]
##arcpy.mapping.AddLayer(Parks, parks, "BOTTOM")
##
###Save to a new map document and clear variable references
##mxd.saveACopy(r"E:\Python Class\Python\Data\Exercise10\Results\B_Carlock_Ch10.mxd")
##del mxd, mxd2


##import arcpy
##mxd = arcpy.mapping.MapDocument(r"E:\Python Class\Python\Data\Exercise10\Austin_TX.mxd")
##df = arcpy.mapping.ListDataFrames(mxd, "New Parks Frame")[0]
##addLayer = arcpy.mapping.Layer(r"E:\Python Class\Python\Data\Exercise10\Austin\parks.shp")
##arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
##mxd.saveACopy(r"E:\Python Class\Python\Data\Exercise10\Results\Austin_TX2.mxd")
##del mxd, addLayer
