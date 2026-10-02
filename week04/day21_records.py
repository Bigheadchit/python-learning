measurements = [
    {"voltage": 4.5, "current": 0.02, "temperature": 30.0},
    {"voltage": 4.4, "current": 0.03, "temperature": 31.0},
    {"voltage": 4.3, "current": 0.04, "temperature": 32.0}
]
measurements.append(
    {"voltage": 4.2, "current": 0.05, "temperature": 33.0}
)
for measurement in measurements:
    current = measurement["current"]
    voltage = measurement["voltage"]
    temperature = measurement["temperature"]
    print("温度：", temperature, "℃")
    power = current*voltage
    print("电流：",current,"A","电压：",voltage,"V","功率：",power,"W")
   
