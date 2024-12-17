import pandas as pd
import matplotlib.pyplot as plt

# data download
file_path = '/Users/martingauss/Desktop/Projects/Contamination/final_contamination.csv'
data = pd.read_csv(file_path)

# Convertation date to datetime
data['datetime'] = pd.to_datetime(data['datetime'])

# making plot 
plt.figure(figsize=(12, 6))

# Curve style of pm10
plt.plot(data['datetime'], data['pm10'], color='blue', linestyle='-', label='PM10 Detector')

# Curve style of mobile_device
plt.plot(data['datetime'], data['mobile_device'], color='orange', linestyle='-', label='Mobile Device')

# Curve style of samples
plt.plot(data['datetime'], data['samples'], color='red', linestyle='-', label='Samples')

# Title and labels
plt.xlabel('Datetime')
plt.ylabel('Contamination Level (particles/hour)')
plt.title('Contamination Levels Comparison: Mobile Device, pm10 Detector and samples')

# Legend and grid
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
