def calculate(voltage,current):
    power = voltage * current
    return power

def save_result(power_w, energy_Wh,charge_Ah,duration_s):
    with open("day35_results.txt","a",encoding="utf-8") as file:
        file.write ("功率："+ str(power_w)+ "W\n")
        file.write ("电能："+ str(energy_Wh)+ "Wh\n")
        file.write ("电量："+ str(charge_Ah)+ "Ah\n")
        file.write ("持续时间："+ str(duration_s)+ "s\n")
try:
    voltage = float(input("请输入电压，V："))
    current = float(input("请输入电流，A："))
    duration_s = float(input("请输入持续时间，s："))

    if duration_s <= 0:
        print("时间必须大于0，本次不计算")
    else:
        power_w = calculate(voltage, current)
        energy_Wh = power_w*duration_s/3600
        charge_Ah = current*duration_s/3600
        save_result(power_w,energy_Wh,charge_Ah,duration_s)
        try:
            with open("day35_results.txt", "r", encoding="utf-8") as file:
                for line in file:
                    print(line, end="")
            print("读取完成")
        except FileNotFoundError:
            print("找不到结果文件，请检查路径")
        print("计算并保存完成")

except ValueError:
    print("输入格式不对，请输入数字")

print("本次程序结束")
