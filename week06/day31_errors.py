try:
    time_text = input("请输入持续时间，s：")
    duration_s = float(time_text)
    duration_h = duration_s / 3600
    print("持续时间：", duration_h, "h")
except ValueError:
    print("输入格式不对，请输入数字，例如600")

print("本次程序结束")

try:
    with open("C:/能源项目学习/第五周/day_results.txt","r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
    print("读取完成")
except FileNotFoundError:
    print("找不到文件，请检查文件名和路径")
