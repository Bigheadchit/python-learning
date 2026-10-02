temperature_text = input("请输入温度，单位℃：")
temperature = float(temperature_text)

if temperature >= 40:
    print("达到或超过练习阈值")
else:
    print("低于练习阈值")

print("本次判断结束")
