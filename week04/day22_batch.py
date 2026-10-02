measurements = [
    {"voltage": 5.0, "current": 0.02, "temperature": 30.0},
    {"voltage": 4.5, "current": 0.02, "temperature": 30.5},
    {"voltage": 4.0, "current": 0.03, "temperature": 31.0},
    {"voltage": 5.0, "current": 0.04, "temperature": 31.5},
    {"voltage": 4.5, "current": 0.04, "temperature": 32.0},
    {"voltage": 4.0, "current": 0.05, "temperature": 32.5},
    {"voltage": 5.0, "current": 0.00, "temperature": 33.0},
    {"voltage": 4.5, "current": 0.06, "temperature": 33.5},
    {"voltage": 4.0, "current": 0.02, "temperature": 34.0},
    {"voltage": 5.0, "current": 0.03, "temperature": 34.5}
]
measurements[6]["current"] = 0.01 
print(len(measurements))
for measurement in measurements:
    current = measurement["current"]
    voltage = measurement["voltage"]
    temperature = measurement["temperature"]
    print("温度：", temperature, "℃")
    power = current*voltage
    print("电流：",current,"A","电压：",voltage,"V","功率：",power,"W")

print("全部记录处理结束")
