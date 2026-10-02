for i in range(5):
    voltage_text = input("请输入电压，V:")
    voltage = float(voltage_text)

    current_text = input("请输入电流，A:")
    current = float(current_text)

    duration_s = input("使用时间，s:")
    duration = float(duration_s)        

    if duration <= 0:
        print("时间不能为0或负数，本次不计算")

    else:
        time = duration/3600
        power = voltage*current
        电量 = current*time
        电能 = power*time
        print("时间：",time,"h")
        print("功率：",power,"W")
        print("电量：",电量,"Ah")
        print("电能：",电能,"Wh")

print("五次测试结束")
    
