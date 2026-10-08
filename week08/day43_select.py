import pandas as pd

measurements = [
    {"voltage_V": 4.8,"current_A":0.02},
    {"voltage_V": 5.0, "current_A": 0.04},
    {"voltage_V": 4.0, "current_A": 0.05}
]

df = pd.DataFrame(measurements)

print(df)
print(df["voltage_V"])

print("前一条记录：")
print(df.head(1))

print("电流列：")
print(df["current_A"])
