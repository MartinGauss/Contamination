import pandas as pd

pm_df = pd.read_csv('pm.csv')
dv_df = pd.read_csv('dv.csv')

merged_df = pd.merge(dv_df, pm_df[['datetime', 'pm10']], on='datetime', how='left')
merged_df.to_csv('merged_contamination_data.csv', index=False)
