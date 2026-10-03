import numpy as np

voltages = np.array([4.5, 5.0, 4.0])
currents_A = np.array([0.02, 0.04, 0.05])

power = voltages*currents_A
print("功率：",power,"W")
