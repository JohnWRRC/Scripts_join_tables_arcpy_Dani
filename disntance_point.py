# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# disntance_point.py
# Created on: 2015-03-23 11:27:20.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy


# Local variables:
d1_wan_c = "d1_wan_c"
d1_wan_c__2_ = "d1_wan_c"
d1_wan_c_PointDistance = "C:\\Users\\John\\Documents\\ArcGIS\\Default.gdb\\d1_wan_c_PointDistance"

# Process: Point Distance
arcpy.PointDistance_analysis(d1_wan_c, d1_wan_c__2_, d1_wan_c_PointDistance, "")

