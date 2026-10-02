voltage_text="5.0"
voltage= float(voltage_text)

print("转换前",voltage_text, type(voltage_text))
print("转换后", voltage , type(voltage))

current = 0.02
power= voltage * current
print("功率：", power ,"W")
