voltage_text = input("请输入电压，单位V:")
voltage = float(voltage_text)
print("你输入的是：",voltage,"V")

current_text = input("请输入电流，单位A：")
current = float(current_text)
print("你输入的是，",current,"A")

power = current*voltage
print("power=",power,"W")
