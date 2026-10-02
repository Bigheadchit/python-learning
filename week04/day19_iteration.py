voltages = [4.50, 4.40, 4.46]
current = 0.02
voltages.append(4.30)
for voltage in voltages:
    print("当前电压：", voltage, "V")
    power = current*voltage
    print("当前功率：",power,"W")
    
print("处理结束")
