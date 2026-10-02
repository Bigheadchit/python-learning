class Measurement:
    pass

record1 = Measurement()
record1.voltage = 4.5
record1.current = 0.02

record2 = Measurement()
record2.voltage = 5.0
record2.current = 0.04

power1 = record1.current*record1.voltage
power2 = record2.current*record2.voltage

print("功率1为",power1,"W")
print("功率2为",power2,"W")

record1.current = 0.03
print("第一条电流：", record1.current, "A")
print("第二条电流：", record2.current, "A")

