voltage_text = input("请输入电压，V：")
voltage = float(voltage_text)
print("电压：", voltage,"V")

current_text = input("请输入电流,A：")
current = float(current_text)
print("电流：",current,"A")

time_text = input("请输入持续时间，s：")
time= float (time_text) /3600
print("持续时间为",time,"h")

power = voltage*current
print("功率：",power,"W")

电量 = current*time
print("电量：",电量,"Ah")

电能 = power*time
print("电能：",电能,"Wh")

电能J = 电能*3600
print("电能J：",电能J,"J")




