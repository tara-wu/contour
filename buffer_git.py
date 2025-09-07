#-------------------------------------------------------------------------------
# Name:        buffer_git.py
# Purpose:     Script uses Contour Tool in ArcGIS Pro to create contour lines
#              for the Fox Lake Quadrangle.
# Author:      Tara Wu
# Created:     07/09/2024
#-------------------------------------------------------------------------------


# import modules
import arcpy
import os


# check out Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# create putput folder if it doesn't exist
os.makedirs("./outputs", exist_ok=True)


# define workspace (relative to script)
arcpy.env.workspace = "./data"
arcpy.env.overwriteOutput = True


try:
    # specify input raster
    in_raster = "./data/foxlake"
    contour_interval = 25
    base_contour = 0
    out_contour = "./outputs/foxlake_contours.shp"

    # Check if raster exists before continuing
    if not os.path.exists(in_raster):
        raise FileNotFoundError(f"Raster not found at {in_raster}. Did you run the script from the repo folder and extract the data correctly?")

    # perform Contour Operation and Save Resulting Data
    Contour(in_raster, out_contour, contour_interval, base_contour)

    # report a success message
    arcpy.AddMessage("Success!")

except Exception as e:
    # report error message
    arcpy.AddError(f"Could not complete contour operation: {e}")

finally:
    arcpy.CheckInExtension("Spatial")
