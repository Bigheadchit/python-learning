time_text = input("请输入持续时间，s：")
time = float(time_text)/3600
def calculate_power(voltage, current):
    power = voltage * current
    return power

power_w = calculate_power(4.5, 0.04)
print("功率：", power_w, "W")
电能_Wh = power_w*time
print("电能：",电能_Wh,"Wh")

with open("day26_result.txt", "w", encoding="utf-8") as file:
    file.write("功率：" + str(power_w) + " W\n")
    file.write("电能：" + str(电能_Wh) + " Wh\n")
print("保存完成")
