import csv

with open("C:/能源项目学习/第七周/measurements.csv","r",encoding="utf-8-sig",newline="")as file:
    reader = csv.DictReader(file)

    for measurement in reader:
        
        voltage = float(measurement["voltage_V"])
        current_mA = float(measurement["current_mA"])
        

        power_mw = current_mA*voltage
        print("功率：",power_mw,"mW")
        print("电流：",current_mA,"mA")
        print("电压：",voltage,"V")

