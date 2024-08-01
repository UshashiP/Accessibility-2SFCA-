##code working fine
import pandas as pd
import math
import numpy as np
import geopandas as gpd
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt

# Load ICFs shapefile
pri_df = gpd.read_file('Intermediate_Care_Facilities.shp').to_crs('epsg:26985')

# Load population shapefile
populations = gpd.read_file('blocks_with_income.shp').to_crs('epsg:26985')
median_population = populations['Total Popu'].median()
populations['Total Popu'] = populations['Total Popu'].replace(0, median_population)

# Calculate supply-to-demand ratio
pri_df['supply_demand_ratio'] = pri_df['BEDS'] / populations['Total Popu']

# Extract centroids
origins_coords = np.array(populations['geometry'].centroid.apply(lambda geom: (geom.x, geom.y)).tolist())
destinations_coords = np.array(pri_df['geometry'].centroid.apply(lambda geom: (geom.x, geom.y)).tolist())

# Calculate distance matrix
dist_matrix = distance_matrix(origins_coords, destinations_coords)

# Normalize distance matrix
normalized_dist_matrix = (dist_matrix - np.min(dist_matrix)) / (np.max(dist_matrix) - np.min(dist_matrix))

# Define inverse distance decay function
d0_time = 900  # 15 minutes in seconds
def inverse_distance_decay(distance, d0=d0_time):
    return 1 / (1 + distance / d0)

# Apply decay function
decay_matrix = np.vectorize(inverse_distance_decay)(normalized_dist_matrix)

# Expand supply-to-demand ratios
supply_demand_ratio = pri_df['supply_demand_ratio']
supply_demand_ratio_expanded = np.repeat(supply_demand_ratio.values.reshape(1, -1), len(populations), axis=0)

# Calculate accessibility scores
accessibility_origin = np.sum(supply_demand_ratio_expanded * decay_matrix, axis=1)
populations['Accessibility'] = accessibility_origin

# Plot results
fig, ax = plt.subplots(figsize=(12, 10))
populations.plot(column='Accessibility', cmap='viridis', linewidth=0.5, edgecolor='white', legend=True, ax=ax)
pri_df.plot(ax=ax, color='red', markersize=5)
ax.set_title('Accessibility for Intermediate Care Facilities in DC', fontsize=16)
ax.set_xlabel('Longitude', fontsize=14)
ax.set_ylabel('Latitude', fontsize=14)
plt.show()
