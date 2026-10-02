voltage_text = input("请输入电压，单位V:")
voltage = float(voltage_text)
print("你输入的是：",voltage,"V")

current_text = input("请输入电流，单位A：")
current = float(current_text)
print("你输入的是，",current,"A")

power = current*voltage
print("power=",power,"W")

time_text = input("请输入时间，单位s:")
duration_s = float(time_text)
duration_h = duration_s / 3600
print("持续时间：",duration_s,"s")
print("持续时间：",duration_h,"h")

charge_ah = current * duration_h
energy_wh = power * duration_h
print("消耗电量：",charge_ah,"Ah")
print("消耗电能：",energy_wh,"Wh")


