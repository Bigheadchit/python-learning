time_text = input("请输入持续时间，s：")
time = float(time_text)
time_h = time/3600

def calculate(voltage,current):
    power = voltage * current
    return power

def save_result(power_w, energy_Wh):
    with open("day_results.txt","a",encoding="utf-8") as file:
        file.write ("功率："+ str(power_w)+ "W\n")
        file.write ("电能："+ str(energy_Wh)+ "Wh\n")

power_w = calculate(5.0,0.04)

energy_Wh = power_w*time_h

save_result(power_w,energy_Wh)

print("保存完成")
