import csv

with open("C:/能源项目学习/第七周/measurements.csv","r",encoding="utf-8-sig",newline="")as file:
    reader = csv.DictReader(file)

    for measurement in reader:
        print(measurement)
