class Measurement:
    pass

record = Measurement()
record.voltage = 4.5
record.current = 0.04

print("电压：", record.voltage, "V")
print("电流：", record.current, "A")

power = record.voltage*record.current
print("功率：",power,"W")


