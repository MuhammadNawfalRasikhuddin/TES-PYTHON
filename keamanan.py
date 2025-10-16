import pandas as pd
data = pd.read_csv("Occupancy_Estimation.csv")
print(data.head())

print("Ukuran dataset (baris, kolom):", data.shape)
print("\nInformasi dataset:")
print(data.info())\

print("\nNilai unik pada S6_PIR:", data['S6_PIR'].unique())
print("Nilai unik pada S7_PIR:", data['S7_PIR'].unique())
print("Nilai unik pada Room_Occupancy_Count:", data['Room_Occupancy_Count'].unique())
