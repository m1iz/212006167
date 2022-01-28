# 使用if语句，判断一个年份是否为闺年，并分别使用数据进行测试，要求覆盖所有分支语句。


year = eval(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0:
    print("%d年是闰年" % year)
elif year % 400 == 0:
    print("%d年是闰年" % year)
else:
    print("%d年不是闰年" % year)
