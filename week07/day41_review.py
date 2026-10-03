import csv

with open("C:/能源项目学习/第七周/measurements.csv",
          "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    with open("day41_results.txt", "w", encoding="utf-8") as result_file:
        for measurement in reader:
            voltage = float(measurement["voltage_V"])
            current_mA = float(measurement["current_mA"])
            current_A = current_mA / 1000

            power_w = voltage * current_A
            print("功率：", power_w, "W")

            result_file.write("功率：" + str(power_w) + " W\n")
