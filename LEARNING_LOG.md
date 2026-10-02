# 学习任务记录

当前已完成第27天；第4周验收已通过，第5周进行中。任务编号不等于日历日期。以下依据保存的代码和对话提交整理，不补造历史提交。

|任务|练习|记录|
|---|---|---|
|day01_print|[代码](week01/day01_print.py)|已提交；部分连续任务保存最终版本|
|day03_variables|[代码](week01/day03_variables.py)|已提交；部分连续任务保存最终版本|
|day04_power|[代码](week01/day04_power.py)|已提交；部分连续任务保存最终版本|
|day06_types|[代码](week02/day06_types.py)|已提交；部分连续任务保存最终版本|
|day07_float|[代码](week02/day07_float.py)|已提交；部分连续任务保存最终版本|
|day08_input|[代码](week02/day08_input.py)|已提交；部分连续任务保存最终版本|
|day09_10_energy|[代码](week02/day09_10_energy.py)|已提交；部分连续任务保存最终版本|
|day11_calculator|[代码](week02/day11_calculator.py)|已提交；部分连续任务保存最终版本|
|day12_13_conditions|[代码](week03/day12_13_conditions.py)|已提交；部分连续任务保存最终版本|
|day14_for|[代码](week03/day14_for.py)|已提交；部分连续任务保存最终版本|
|day15_while|[代码](week03/day15_while.py)|已提交；部分连续任务保存最终版本|
|day16_validation|[代码](week03/day16_validation.py)|已提交；部分连续任务保存最终版本|
|day17_review|[代码](week03/day17_review.py)|已提交；部分连续任务保存最终版本|
|day18_list|[代码](week04/day18_list.py)|已提交；部分连续任务保存最终版本|
|day19_iteration|[代码](week04/day19_iteration.py)|已提交；部分连续任务保存最终版本|
|day20_dictionary|[代码](week04/day20_dictionary.py)|已提交；部分连续任务保存最终版本|
|day21_records|[代码](week04/day21_records.py)|已提交；部分连续任务保存最终版本|
|day22_batch|[代码](week04/day22_batch.py)|已提交；部分连续任务保存最终版本|

第21天列表与字典组合练习接受了逐步提示；第4周笔记已补齐。代码保留当时版本，运行结果来自学习提交，不表示所有文件已在本次重新运行。

## 第23天验收

[代码](week04/day23_review.py)｜[第4周笔记](notes/第4周学习笔记.txt)

10条记录、40.0与40.1触发练习阈值、第7条0.01A及0.05W、结束提示仅一次。列表/字典/浮点数通过type输出补充确认。依据学生提交代码和输出静态核对，辅导者未代运行。

## 第24天：函数定义与调用

[代码](week05/day24_function.py)

实际用时自述20分钟。三次输出0.1 W、0.18 W、0.2 W正确；理解只定义不调用不会输出，参数按位置传给voltage和current。依据提交代码和运行输出静态核对，辅导者未代运行。验收通过。

## 第25天：返回值与后续计算

[代码](week05/day25_return.py)

用时自述40分钟。正常输出：5.0V、0.02A、600s得到0.1W和约0.016667Wh；4.5V、0.04A、1200s得到0.18W和0.06Wh。初次把返回的功率误作电能，经提示将电能计算移到函数外。用print替代return时，接收变量为None，与float相乘触发TypeError；已恢复return，本地保存代码也确认恢复。理解print显示结果、return将结果交回调用处。依据提交输出和代码静态核对，辅导者未代运行。验收通过。

## 第26天：文本文件写入

[代码](week05/day26_save.py)｜[600秒结果样例](week05/day26_result.txt)

实际用时10分钟。1200秒保存0.18W、0.06Wh；600秒重新运行后文件更新为0.18W、0.03Wh，验证w模式覆盖。理解str将数字转为字符串；准确说是文本文件的write接收字符串，open负责打开文件。曾混淆/n与\n，经示例纠正。依据提交代码、输出及实际保存文件核对，辅导者未代运行。验收通过。

## 第27天：追加写入与文件位置

[代码](week05/day27_append.py)｜[两组结果样例](week05/day27_results.txt)

实际用时5分钟。1200秒和600秒记录同时保留，分别为0.18W/0.06Wh与0.18W/0.03Wh。已确认文件位于本地第5周学习文件夹；理解a追加、w覆盖，input返回字符串所以time_text不需再转换。依据提交代码、回答和实际文件静态核对，辅导者未代运行。验收通过。
