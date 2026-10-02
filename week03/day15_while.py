answer = "y"

while answer == "y":
    T_text = input("请输入温度,单位℃：")
    T = float(T_text)
    if T >= 40:
        print("以达到或超过练习阈值")
    else:
        print("低于联系阈值")

    answer = input("是否继续循环？输入y继续，其他内容结束：")

print("测试结束")
