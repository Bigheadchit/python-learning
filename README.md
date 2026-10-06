# Python 学习记录

记录Python基础、文件读写、CSV、NumPy与Pandas数据处理练习，逐步用于能源设备自动测试项目。

|学习周|内容|
|---|---|
|[第1周](week01)|输出、变量与功率计算|
|[第2周](week02)|输入、类型转换与Ah / Wh / J计算|
|[第3周](week03)|条件判断、循环与输入检查|
|[第4周](week04)|列表、字典与批量记录处理|
|[第5周](week05)|函数、返回值与文本文件保存|
|[第6周](week06)|文件读取、异常处理、类与对象|
|[第7周](week07)|CSV读取、单位换算、NumPy计算与结果保存|
|[第8周](week08)|Pandas建表与列数据读取|

完成Pandas建表、读取电压列和修改测量数据。

[学习记录](LEARNING_LOG.md) · [每周笔记](notes)

## 运行

使用Python 3.13.15和IDLE，打开练习文件后按F5运行；NumPy练习使用2.5.3版本。

```text
py -3.13 -m pip install numpy==2.5.3
py -3.13 -m pip install pandas
```

CSV数据位于[week07/measurements.csv](week07/measurements.csv)，运行前将代码中的本地路径改为实际文件位置；第30—31天读取[week05/day_results.txt](week05/day_results.txt)。

练习数据为手动输入或模拟数据，Ah和Wh按恒定电压、电流计算；任务编号按学习顺序排列，早期代码集中整理上传。
