import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data
particle_data = {
    'Particle Size (μm)': [5, 15, 25, 50, 100, 150],  # Particle size in μm
    'Quantity': [7, 3, 0, 0, 0, 0]  # Number of particles
}

# Convert data to DataFrame
particle_df = pd.DataFrame(particle_data)

# Calculate the area of each particle (assume circular shape, A = π * r²)
particle_df['Area (μm²)'] = np.pi * (np.array(particle_df['Particle Size (μm)']) / 2)**2

# Calculate the total area for each particle size (area * quantity)
particle_df['Total Area (μm²)'] = particle_df['Area (μm²)'] * particle_df['Quantity']

# Calculate the cumulative total area
particle_df['Cumulative Total Area (μm²)'] = particle_df['Total Area (μm²)'].cumsum()

# Calculate the total area of all particles
total_particle_area = particle_df['Total Area (μm²)'].sum()

# Total surface area in μm² (for 2.68 cm²)
area_in_cm2 = 2.68  # Surface area in cm²
area_in_um2 = area_in_cm2 * 1e8  # Convert to μm²

# Calculate contamination in ppm
contamination_ppm = (total_particle_area / area_in_um2) * 1e6

# Calculate cumulative contamination in ppm
particle_df['Cumulative PPM'] = (particle_df['Cumulative Total Area (μm²)'] / area_in_um2) * 1e6

# Display results
print("Total particle area (μm²):", total_particle_area)
print("Total surface area (μm²):", area_in_um2)
print("Contamination (ppm):", contamination_ppm.round(3))
print(particle_df)
