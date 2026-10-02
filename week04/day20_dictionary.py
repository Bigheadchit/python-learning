measurement = {
    "voltage": 4.5,
    "current": 0.02,
    "temperature": 30.0
}

print(measurement)
power = measurement["voltage"] * measurement["current"]
print("修改前功率：", power, "W")
measurement["current"] = 0.04

print("电压：",measurement["voltage"],"V")
print("电流：", measurement["current"], "A")
print("温度：", measurement["temperature"], "℃")

power = measurement["voltage"]*measurement["current"]
print("功率：",power,"W")
