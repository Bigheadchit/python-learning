time_text = input("请输入持续时间，s：")
time = float(time_text)/3600
def calculate_power(voltage, current):
    power = voltage * current
    return power

power_w = calculate_power(4.5, 0.04)
print("功率：", power_w, "W")
电能_Wh = power_w*time
print("电能：",电能_Wh,"Wh")
