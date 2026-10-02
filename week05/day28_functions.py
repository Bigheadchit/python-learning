time_text = input("请输入持续时间，s：")
duration_s = float(time_text)
duration_h = duration_s / 3600

def calculate_power(voltage, current):
    power = voltage * current
    return power


def save_result(power_w, energy_wh):
    with open("day28_results.txt", "a", encoding="utf-8") as file:
        file.write("功率：" + str(power_w) + " W\n")
        file.write("电能：" + str(energy_wh) + " Wh\n")

power_w = calculate_power(4.5, 0.04)
energy_wh = power_w * duration_h

save_result(power_w, energy_wh)
print("保存完成")
