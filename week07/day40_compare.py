import numpy as np

voltages = np.array([4.5, 5.0, 4.0])
currents_A = np.array([0.02, 0.04, 0.05])

print("数组计算：", voltages * currents_A, "W")

for i in range(len(voltages)):
    power = voltages[i]*currents_A[i]
    print("循环计算：",power,"W")
