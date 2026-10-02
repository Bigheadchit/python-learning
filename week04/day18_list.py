voltages = [4.50, 4.40, 4.46]

print("全部电压：", voltages)
print("第一个电压：", voltages[0], "V")
print("第二个电压：", voltages[1], "V")
print("第三个电压：", voltages[2], "V")
print("数据数量：", len(voltages))

current_text = 0.02
current = float(current_text)
power=voltages[0]*current
print("功率：",power,"W")
