for i in range(3):
    T_text= input("请输入温度，℃：")
    T = float(T_text)
    if T >=  40:
        print("达到或超越测试温度")
    else:
        print("未达到测试温度")

print("三次判断全部结束")
