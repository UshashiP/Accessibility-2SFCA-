# Accessibility-2SFCA-
This repository contains a Python script to calculate the accessibility of Intermediate Care Facilities (ICFs) in Washington, D.C., using the 2-Step Floating Catchment Area (2SFCA) method. The analysis involves using population and ICF data, calculating supply-to-demand ratios, and visualizing the accessibility scores on a map.

Introduction
The 2SFCA method is a popular approach for measuring spatial accessibility. This project aims to apply the 2SFCA method to evaluate the accessibility of Intermediate Care Facilities in Washington, D.C., taking into account the distribution of population and the number of available beds in each facility.

Installation
To run the script, you need to have Python installed along with the following libraries:
pandas
numpy
geopandas
scipy
matplotlib

Data
The analysis requires two shapefiles:

Intermediate_Care_Facilities.shp: Contains the locations and attributes of ICFs, including the number of beds.
blocks_with_income.shp: Contains the locations and population data of census blocks.

Methodology
The script follows these steps to calculate the accessibility scores:
Load Data: Load ICF and population data, and transform their coordinate reference systems.
Calculate Supply-to-Demand Ratios: Compute the ratio of the number of beds to the population for each ICF.
Distance Matrix Calculation: Calculate the distance matrix between population centroids and ICF centroids, and normalize it.
Decay Function: Apply an inverse distance decay function to model the effect of distance on accessibility.
Accessibility Calculation: Multiply the supply-to-demand ratios by the decay matrix and sum the results to get the accessibility scores for each population centroid.
Visualization: Plot the accessibility scores on a map, with ICF locations overlaid.

Results
The script outputs a map visualizing the accessibility scores for each census block, with higher scores indicating better accessibility to ICFs. The map also shows the locations of ICFs.


